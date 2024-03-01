import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import json


def load_and_preprocess_data(file_path, features, target):
    with open(file_path, "r") as file:
        data = json.load(file)

    # Flatten Json to dataframe
    rows = []
    for item in data:
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

    df = pd.DataFrame(rows)

    X = df[features]
    y = df[target]

    return X, y


def train_and_evaluate_model(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = RandomForestClassifier(n_estimators=100, random_state=random_state)

    # Train model
    model.fit(X_train, y_train)

    # Make prediction
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy:", accuracy)


# Define file path to train
file_path = "/home/student/juniorsem/SEERS/scripts/analyzer/combined_result.json"
features = ["lineno", "coloffset", "min", "max", "tests", "failures"]
target = "errors"

# Load and preprocess the data
X, y = load_and_preprocess_data(file_path, features, target)

# Train and evaluate the model
train_and_evaluate_model(X, y)

# Define file path for the new JSON file
compare_file_path = "/home/student/juniorsem/SEERS/test.json"

# Load and preprocess the new data
compare_x, compare_y = load_and_preprocess_data(compare_file_path, features, target)

# Train and evaluate the model using the new data
train_and_evaluate_model(compare_x, compare_y)
