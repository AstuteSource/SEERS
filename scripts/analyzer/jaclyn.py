import pandas as pd
from sapientml.sapientml import SapientML
from sapientml.sapientml.util.logging import setup_logger
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Convert JSON to CSV file type using pandas
json_file_path = "combined_result.json"
df = pd.read_json(json_file_path)
#Display the DF
print(df.head())
# Convert DataFrame to CSV and save it
csv_file_path = 'testFile.csv'
df.to_csv(csv_file_path, index = False)
print(f"Successfully convert {json_file_path} to {csv_file_path}. Begin training the model...")

#Load Dataset
train_data = pd.read_csv(csv_file_path)
train_data,test_data = train_test_split(train_data)

#Split the dataset into train and test data 
y_true = test_data[""mutmut_result""]