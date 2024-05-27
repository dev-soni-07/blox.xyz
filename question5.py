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

account_A = BankAccount('User A', 1000)
account_B = BankAccount('User B', 500)

transfer1 = threading.Thread(target=transfer_money, args=(account_A, account_B, 200))
transfer2 = threading.Thread(target=transfer_money, args=(account_B, account_A, 150))

transfer1.start()
transfer2.start()

transfer1.join()
transfer2.join()