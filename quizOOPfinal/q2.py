class BankAccount:
    def __init__(self, account_number: str, owner_name: str, balance: float = 0.0) -> None:
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        
    def deposit(self, amount: float) -> None:
        self.amount = amount
        self.amount += self.balance
        print(f"Deposited: {self.amount:.2f}")
        
    def withdraw(self, amount: float) -> None:
        self.amount = amount
        self.amount -= self.balance
        return (f'Withdrawn: {self.amount:.2f}')
        
    def display(self) -> None:
        return f'Account created for {self.owner_name}\nDeposited: {}\nWithdrawn: {}\nBalance: {self.balance:.2f}'
    
    
owner_name = input("Name: ")
account_number = input("Account: ")

ba = BankAccount(account_number,owner_name)
print(ba.display())