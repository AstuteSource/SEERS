import pandas as pd
import json


def pandaJSON(data):
	with open(data) as file:    
	    json_data = json.load(file) 
	print(pd.json_normalize(json_data))



def main():
	df = pandaJSON("combined_result.json")
	print(df)


if __name__ == '__main__':
    main()
