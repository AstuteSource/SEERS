import pandas as pd
import json


def pandaJSON(data):
	with open(data) as file:    
		json_data = json.load(file) 
	df = pd.json_normalize(json_data)
	return df


def main():
	frame = pandaJSON("combined_result.json")
	print(frame)
	frame.to_excel("out.xlsx")


if __name__ == '__main__':
    main()
