import pandas as pd
import json
from sapientml import SapientML
from sapientml.util.logging import setup_logger
from sklearn.metrics import f1_score
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Convert JSON to CSV file type using pandas
def json_to_csv(json_file_path, csv_file_path='output.csv'):
    # Load JSON data and normalize
    with open(json_file_path) as file:
        json_data = json.load(file)
    df = pd.json_normalize(json_data)
    # Display the DataFrame
    print(df.head())
    # Convert DataFrame to CSV and save
    df.to_csv(csv_file_path, index=False)
    print(f"Successfully converted {json_file_path} to {csv_file_path}. Begin training the model...")
    return csv_file_path

def train_and_evaluate_model(csv_file_path):
    # Load data
    train_data = pd.read_csv(csv_file_path)

    # Split data into training and testing sets
    train_data, test_data = train_test_split(train_data)

    # Extract true labels for evaluation
    y_true = test_data["mutmut_result"].reset_index(drop=True)
    test_data.drop(["mutmut_result"], axis=1, inplace=True)

    # Initialize SapientML model
    cls = SapientML(["mutmut_result"])
    
    # Setup logging
    setup_logger().handlers.clear()  # to prevent duplication of logging
    
    # Fit the model on training data
    cls.fit(train_data)

    # Make predictions on test data
    y_pred = cls.predict(test_data)
    y_pred = y_pred["mutmut_result"].rename("mutation_pred")

    # Concatenate true and predicted values
    result_df = pd.concat([y_pred, y_true], axis=1)

    # Print f1 and R2 score
    print(f"F1 score: {f1_score(y_true, y_pred)}")
    print(f"R2 score: {r2_score(y_true, y_pred)}")

    # Print final script
    print(cls.model.files["final_script.py"].decode("utf-8"))


def main():
    json_file_path = "output_with_functions.json"
    csv_file_path = json_to_csv(json_file_path)
    train_and_evaluate_model(csv_file_path)

if __name__ == '__main__':
    main()