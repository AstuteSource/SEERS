import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sapientml import SapientML
import json


def pandaJSON(data):
	with open(data) as file:    
		json_data = json.load(file) 
	df = pd.json_normalize(json_data)
	df["mutation_score"] = (df["mutmut_summary.tests"]-df["mutmut_summary.failures"]) / df["mutmut_summary.tests"]
	return df


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
