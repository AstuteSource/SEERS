import pandas as pd
import json
from sapientml import SapientML
from sapientml.util.logging import setup_logger
from sklearn.metrics import f1_score
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


def load_data(json_file_path):
    with open(json_file_path) as file:
        json_data = json.load(file)

    # Flatten Json to dataframe
    rows = []
    for item in json_data:
        row = {
            "file": item["file"],
            "lineno": item["pattern"]["lineno"],
            "coloffset": item["pattern"]["coloffset"],
            "linematch": item["pattern"]["linematch"],
            "min": item["pattern"]["min"],
            "max": item["pattern"]["max"],
            "tests": item["mutmut_summary"]["tests"],
            "failures": item["mutmut_summary"]["failures"],
            "errors": item["mutmut_summary"]["errors"],
        }
        rows.append(row)

    data = pd.DataFrame(rows)
    print("DataFrame:")
    print(data.head())
    print(data.columns)
    return data


def train_and_evaluate_model(data):
    # Split data into training and testing sets
    train_data, test_data = train_test_split(data)

    # Extract true labels for evaluation
    y_true = test_data["failures"].reset_index()

    # Initialize SapientML model
    cls = SapientML(["failures"])

    # Setup logging
    setup_logger().handlers.clear()  # to prevent duplication of logging

    # Fit the model on training data
    cls.fit(train_data)

    # Make predictions on test data
    y_pred = cls.predict(test_data)
    y_pred = y_pred["failures"].rename("failure_pred")

    # Concatenate true and predicted values
    result_df = pd.concat([y_pred, y_true], axis=1)

    # Print f1 and R2 score
    print(f"F1 score: {f1_score(y_true, y_pred)}")
    print(f"R2 score: {r2_score(y_true, y_pred)}")

    # Print final script
    print(cls.model.files["final_script.py"].decode("utf-8"))


def main():
    json_file_path = "output_with_functions.json"
    data = load_data(json_file_path)
    train_and_evaluate_model(data)


if __name__ == "__main__":
    main()
