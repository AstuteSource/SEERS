import pandas as pd

# Read the JSON file into a DataFrame
json_file_path = "testFile.json"
df = pd.read_json(json_file_path)
df_flattened = pd.json_normalize(df,sep='_')
#Display the DF
print(df_flattened.head())

# Convert DataFrame to CSV and save it
csv_file_path = 'testFile.csv'
df.to_csv(csv_file_path, index = False)

print(f"Succesfully convert {json_file_path} to {csv_file_path}. Begin training the model...")