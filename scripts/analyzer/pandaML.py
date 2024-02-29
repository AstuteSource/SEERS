import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sapientml import SapientML
import json
from automl.sapientml.sapientml.main import SapientML
from sklearn.model_selection import train_test_split

def load_data(data):
    with open(data) as file:
        json_data = json.load(file)
    df = pd.json_normalize(json_data)
    return df


def pandaJSON(data):
	with open(data) as file:    
		json_data = json.load(file) 
	df = pd.json_normalize(json_data)
	df["mutation_score"] = (df["mutmut_summary.tests"]-df["mutmut_summary.failures"]) / df["mutmut_summary.tests"]
	return df


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

def sapient(dataframe):
	cls = SapientML(
	    target_columns=["mutation_score"],
	    task_type=None, 
	)
	dataframe, test_data = train_test_split(dataframe)
	y_true = test_data["mutation_score"].reset_index(drop=True)
	test_data.drop("mutation_score", axis=1, inplace=True)
	cls.fit(dataframe, output_dir="./outputs")
	y_pred = cls.predict(test_data)
	return f1_score(y_true,y_pred)


def main():
	frame = pandaJSON("combined_result.json")
	print(sapient(frame))


if __name__ == '__main__':
    main()
