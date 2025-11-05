class BankAccount:
    def __init__(self, owner, balance=0, interest_rate=0.01):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount.")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"Interest added: {interest}")
        print(f"Interest of {interest} added. New balance: {self.balance}")

    def show_transactions(self):
        print("Transaction History:")
        for t in self.transactions:
            print(" -", t)

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"



