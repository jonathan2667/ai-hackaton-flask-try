# app.py

from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load fake data
accounts_df = pd.read_csv('fake_accounts.csv')
transactions_df = pd.read_csv('fake_transactions.csv')

# Load the classifier, label encoder, and feature names
with open('classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)
with open('label_encoder.pkl', 'rb') as le_file:
    le = pickle.load(le_file)
with open('feature_names.pkl', 'rb') as fn_file:
    feature_names = pickle.load(fn_file)

@app.route('/')
def index():
    user_profile = generate_user_profile('user_id_1')  # Replace with logic to select a specific user
    return render_template('index.html', user_profile=user_profile)

def generate_user_profile(user_id):
    # Example logic to generate a user profile
    user_account = accounts_df.iloc[0].to_dict()  # Replace with logic to select a specific user's account
    user_transactions = transactions_df[transactions_df['account_id'] == user_account['account_id']].to_dict(orient='records')
    
    # Classify transactions
    classified_transactions = classify_transactions(user_transactions)
    
    user_profile = {
        'account': user_account,
        'transactions': classified_transactions
    }
    return user_profile

def classify_transactions(transactions):
    for txn in transactions:
        txn_type_encoded = le.transform([txn['transaction_type']])[0]
        txn_features = pd.DataFrame([[txn['amount'], txn_type_encoded]], columns=feature_names)
        txn['category'] = classifier.predict(txn_features)[0]
    
    return transactions

if __name__ == '__main__':
    app.run(debug=True)
