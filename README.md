# Blox.xyz Assignment

## Overview
This repository contains solutions to the Blox.xyz backend assignment.

## Question 1: Mandatory

### Internship or Academic Projects
1. **What did the system do?**
   - **Project:** "Ease My Order" - A Restaurant Order & Billing System.
   - **Functionality:** Allows users to browse the menu, place orders, and generate bills automatically.

2. **Similar Systems in the Wild**
   - Restaurant POS (Point of Sale) systems, which manage orders, billing, and sometimes inventory management.

3. **Approach to Development**
   - Defined system requirements and functionalities.
   - Used Python and libraries like Pandas, NumPy, and Matplotlib for data integration and analysis.
   - Thoroughly tested each feature for accuracy and efficiency.

4. **Interesting Aspects from Stack Overflow**
   - Snippets for reading and processing CSV files efficiently.
   - Implementing a simple menu-driven interface and data visualization for bill summaries.

5. **Learnings from Specific Copy-Paste**
   - Handling various data formats and ensuring data integrity.
   - Structuring user interactions clearly in menu interfaces.
   - Importance of optimizing code for performance and user experience.

## Question 3: JSON Parsing in Python

### Description
The Python function `parse_json` converts a JSON string into a corresponding Python object such as a dictionary, list, or basic data types. It uses Python's built-in `json` module to handle numbers with high precision using the `Decimal` class from the `decimal` module. It provides clear error messages if the JSON is invalid.

### Code
```python
import json
from decimal import Decimal

def parse_json(json_string):
    try:
        result = json.loads(json_string, parse_float=Decimal, parse_int=Decimal)
        return result
    except json.JSONDecodeError as e:
        return f"Invalid JSON: {str(e)}"

# Example usage
json_string = '{"name": "John", "age": 30, "balance": 12345.67}'
print("Valid JSON example:")
result = parse_json(json_string)
print(result)

invalid_json_string = '{"name": "John", "age": 30, "balance": 12345.67'
print("\nInvalid JSON example:")
result = parse_json(invalid_json_string)
print(result)
```

## Question 5: Banking System Simulation

### Description
This code simulates transferring money between two bank accounts, potentially in different banks. It addresses concurrency, transaction atomicity, and security issues by using threading and locks.

### Issues in the System
1. **Concurrency:** Simultaneous transactions may interfere with each other.
2. **Rollback:** Ensuring the withdrawn amount is returned if a deposit fails.
3. **Security:** Protecting transactions from fraud or errors.

### Mitigations
1. **Threading:** Handling multiple transactions simultaneously while managing interactions carefully.
2. **Atomic Transactions:** Ensuring transactions roll back entirely if any part fails.
3. **Logging:** Keeping a log of transactions for troubleshooting and security checks.

### Code
```python
import threading
import time

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            return True

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                return True
            return False

def transfer_money(from_account, to_account, amount):
    transaction_id = time.time()
    print(f"Trying to transfer ${amount} from {from_account.owner} to {to_account.owner} with transaction ID: {transaction_id}")
    
    if from_account.withdraw(amount):
        if to_account.deposit(amount):
            print(f"Success: ${amount} was transferred from {from_account.owner} to {to_account.owner}")
        else:
            print(f"Failed to deposit in {to_account.owner}'s account. Rolling back transaction.")
            from_account.deposit(amount)
    else:
        print(f"Failed: Not enough money in {from_account.owner}'s account to transfer.")

# Creating bank accounts
account_A = BankAccount('User A', 1000)
account_B = BankAccount('User B', 500)

# Threads to simulate transferring money between accounts
transfer1 = threading.Thread(target=transfer_money, args=(account_A, account_B, 200))
transfer2 = threading.Thread(target=transfer_money, args=(account_B, account_A, 150))

transfer1.start()
transfer2.start()

transfer1.join()
transfer2.join()
```

## Author
DEV SONI
