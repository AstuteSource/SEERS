# *** GENERATED PIPELINE ***

# LOAD DATA
import pandas as pd
train_dataset = pd.read_pickle("./training.pkl")

import pickle


# DISCARD IRRELEVANT COLUMNS
irrelevant_columns = ['function_name', 'function_scope']
train_dataset = train_dataset.drop(irrelevant_columns, axis=1, errors="ignore")

# PREPROCESSING-1
import re
import string
import nltk
TEXT_COLUMNS = ['mutants', 'patterns']
def process_text(__dataset):
    for _col in TEXT_COLUMNS:
        process_text = [t.lower() for t in __dataset[_col]]
        # strip all punctuation
        table = str.maketrans('', '', string.punctuation)
        process_text = [t.translate(table) for t in process_text]
        # convert all numbers in text to 'num'
        process_text = [re.sub(r'\d+', 'num', t) for t in process_text]
        __dataset[_col] = process_text
    return __dataset
train_dataset = process_text(train_dataset)

# DETACH TARGET
TARGET_COLUMNS = ['mutation_category']
feature_train = train_dataset.drop(TARGET_COLUMNS, axis=1)
target_train = train_dataset[TARGET_COLUMNS].copy()

# PREPROCESSING-2
from sklearn.preprocessing import OneHotEncoder
CATEGORICAL_COLS = ['check_ids', 'pattern_bool', 'pattern_existence', 'unique_patterns']
onehot_encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
train_encoded = pd.DataFrame(onehot_encoder.fit_transform(feature_train[CATEGORICAL_COLS]), columns=onehot_encoder.get_feature_names_out(), index=feature_train.index)
feature_train = pd.concat([feature_train, train_encoded ], axis=1)
feature_train.drop(CATEGORICAL_COLS, axis=1, inplace=True)
with open('oneHotEncoder.pkl', 'wb') as f:
    pickle.dump(onehot_encoder, f)

# PREPROCESSING-3
from sklearn.feature_extraction.text import TfidfVectorizer
TEXT_COLUMNS = ['mutants', 'patterns']
temp_train_data = feature_train[TEXT_COLUMNS]
# Make the entire dataframe sparse to avoid it converting into a dense matrix.
feature_train = feature_train.drop(TEXT_COLUMNS, axis=1).astype(pd.SparseDtype('float64', 0))
vectorizers = {}
for _col in TEXT_COLUMNS:
    tfidfvectorizer = TfidfVectorizer(max_features=3000)
    vector_train = tfidfvectorizer.fit_transform(temp_train_data[_col])
    feature_names = ['_'.join([_col, name]) for name in tfidfvectorizer.get_feature_names_out()]
    vector_train = pd.DataFrame.sparse.from_spmatrix(vector_train, columns=feature_names, index=temp_train_data.index)
    feature_train = pd.concat([feature_train, vector_train], axis=1)
    vectorizers[_col] = tfidfvectorizer
with open('tfidfVectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizers, f)

# MODEL
import numpy as np
from sklearn.linear_model import LogisticRegression
random_state_model = 42
model = LogisticRegression(random_state=random_state_model, )
model.fit(feature_train, target_train.values.ravel())
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
