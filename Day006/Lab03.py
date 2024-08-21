# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance

# Create an instance of BankAccount with an initial balance of 1000
account = BankAccount(1000)

# Deposit 500
account.deposit(500)

# Print the current balance
print(account.get_balance())
