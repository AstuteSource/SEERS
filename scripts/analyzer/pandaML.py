import pandas as pd
import json
from automl.sapientml.sapientml.main import SapientML
from sklearn.model_selection import train_test_split

def load_data(data):
    with open(data) as file:
        json_data = json.load(file)
    df = pd.json_normalize(json_data)
    return df

def define_mutation_score(mutant_data)->int:
    # Define the 'mutation_score' based on the presence of 'failure' in 'mutants'
    return 1 if 'failure' in mutant_data else 0

def train_and_evaluate_model(data):
    # Load data
    frame = load_data(data)

    # Extract features and define 'mutation_score'
    # Features are the inputs variable for the model, 'mutation_score" is the label we want to predict
    features = frame.drop(columns=['mutants']) # Drop column as it's not a feature.
    frame['mutation_score'] = frame['mutants'].apply(define_mutation_score) # Define `mutation_score` from function above
    labels = frame['mutation_score']

    # Split the data into training and testing sets, assess the model's performance on unseen data
    # So dividing our dataset into two subsets (`X_train`, `Y_train`) and (`X_test`,`Y_test`)
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Initialize AutoML
    ml =SapientML()

    # Train the machine learning model
    model = ml.fit(X_train, y_train)

    # Evaluate the model
    evaluation_metrics = ml.evaluate(X_test, y_test)
    print("Evaluation Metrics:")
    print(evaluation_metrics)

    # Extract feature importance, insights into what aspects of the data are critical for determining `mutation_score`
    feature_importance = ml.feature_importance()
    print("Feature Importance:")
    print(feature_importance)

def main():
    train_and_evaluate_model("combined_result.json")

if __name__ == '__main__':
    main()
