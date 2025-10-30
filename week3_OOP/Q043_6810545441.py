# Name: Krittitee Chaisang #  Student ID: 6810545441
name = input("Enter account owner: ")
balance = input("Enter initial balance: ")
print(f"Welcome, {name}.")
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance
        
    def get_balance(self):
        return f"Current balance: {self.__balance:.2f}"
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful. New balance: {self.__balance:.2f}"
        else:
            return 'Invalid deposit amount.'
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrawal successful. New balance: {self.__balance:.2f}"
        else:
            return f"Insufficient funds or invalid amount."
        
acc = BankAccount(name, balance)        
while True:
    cmd = input("Enter command: ").split()
    try:
        action = cmd[0]
        val = float(cmd[1])
    except ValueError:
        val = None
    if action == 'exit':
        print("Goodbye.")
    elif action == 'deposit' and val != None:
        print(acc.deposit())
    elif action == 'withdraw' and val != None:
        print(acc.withdraw())
    elif action == 'balance' and val == None:
        print(acc.get_balance())
    else:
        print()