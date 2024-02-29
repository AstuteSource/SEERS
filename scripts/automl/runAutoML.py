import pandas as pd
from sapientml.sapientml import SapientML
# `f1_score` from scikit-learn to evaluate the model's performance
from sklearn.metrics import f1_score
# `train_test_split` is used to split the data into training and testing sets
from sklearn.model_selection import train_test_split

# Convert JSON to CSV file type using pandas
json_file_path = "testFile.json"
df = pd.read_json(json_file_path)
#Display the DF
print(df.head())
# Convert DataFrame to CSV and save it
csv_file_path = 'testFile.csv'
df.to_csv(csv_file_path, index = False)
print(f"Successfully convert {json_file_path} to {csv_file_path}. Begin training the model...")

#read csv file
df = pd.read_csv(csv_file_path)

df = df.rename(columns={
    'file': 'file_path',
    'pattern_lineno': 'pattern_line_number',
    'pattern_coloffset': 'pattern_column_offset',
    'pattern_linematch': 'pattern_line_match',
    'pattern_context': 'pattern_context',
    'pattern_min': 'pattern_min',
    'pattern_max': 'pattern_max',
    'pattern_pattern': 'pattern_xpath_pattern',
    'check_id': 'check_identifier',
    'check_name': 'check_name',
    'mutant_name': 'mutant_name',
    'mutant_line': 'mutant_line_number',
    'mutant_description': 'mutant_description',
    'mutant_failure': 'mutant_failure'
})
df['has_mutant'] = df['mutants'].apply(lambda x: 1 if x else 0)



