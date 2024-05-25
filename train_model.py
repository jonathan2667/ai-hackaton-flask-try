# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pickle

# Load the fake transactions data
transactions_df = pd.read_csv('fake_transactions.csv')

# Simplify the problem by classifying transactions into broad categories
def categorize_transaction(transaction_type):
    if transaction_type in ['Deposit', 'Payment']:
        return 'Income'
    else:
        return 'Expense'

# Apply the categorization
transactions_df['category'] = transactions_df['transaction_type'].apply(categorize_transaction)

# Encode the transaction type
le = LabelEncoder()
transactions_df['transaction_type_encoded'] = le.fit_transform(transactions_df['transaction_type'])

# Split the data into training and testing sets
X = transactions_df[['amount', 'transaction_type_encoded']]
y = transactions_df['category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple classifier
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Save the model and label encoder to disk
with open('classifier.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)
with open('label_encoder.pkl', 'wb') as le_file:
    pickle.dump(le, le_file)

print("Model and label encoder have been saved to disk.")
