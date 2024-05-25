import random
import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Define account types and transaction types
account_types = ['Checking', 'Savings', 'Credit Card']
transaction_types = ['Deposit', 'Withdrawal', 'Purchase', 'Payment', 'Transfer']


# Generate a single fake bank account
def generate_fake_account():
    account = {
        'account_id': fake.uuid4(),
        'account_type': random.choice(account_types),
        'balance': round(random.uniform(1000, 100000), 2),
        'currency': 'USD',
        'transactions': generate_fake_transactions()
    }
    return account


# Generate fake transactions for an account
def generate_fake_transactions(num_transactions=50):
    transactions = []
    for _ in range(num_transactions):
        transaction = {
            'transaction_id': fake.uuid4(),
            'date': fake.date_this_year(),
            'transaction_type': random.choice(transaction_types),
            'amount': round(random.uniform(5, 5000), 2),
            'description': fake.sentence(nb_words=6)
        }
        transactions.append(transaction)
    return transactions


# Generate multiple fake bank accounts
def generate_fake_accounts(num_accounts=10):
    accounts = []
    for _ in range(num_accounts):
        accounts.append(generate_fake_account())
    return accounts


# Convert the data to a Pandas DataFrame for easier handling
def accounts_to_dataframe(accounts):
    account_list = []
    transaction_list = []

    for account in accounts:
        account_info = {
            'account_id': account['account_id'],
            'account_type': account['account_type'],
            'balance': account['balance'],
            'currency': account['currency']
        }
        account_list.append(account_info)

        for transaction in account['transactions']:
            transaction_info = {
                'account_id': account['account_id'],
                'transaction_id': transaction['transaction_id'],
                'date': transaction['date'],
                'transaction_type': transaction['transaction_type'],
                'amount': transaction['amount'],
                'description': transaction['description']
            }
            transaction_list.append(transaction_info)

    accounts_df = pd.DataFrame(account_list)
    transactions_df = pd.DataFrame(transaction_list)

    return accounts_df, transactions_df


# Generate and save fake accounts data
num_accounts = 100  # Adjust the number of accounts as needed
accounts = generate_fake_accounts(num_accounts)
accounts_df, transactions_df = accounts_to_dataframe(accounts)

# Save to CSV files
accounts_df.to_csv('fake_accounts.csv', index=False)
transactions_df.to_csv('fake_transactions.csv', index=False)

print("Fake bank accounts and transactions data generated and saved to CSV files.")
