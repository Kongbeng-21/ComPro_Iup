from bank import BankAccount

def main():
    account = BankAccount("Alice", 100, 0.05)
    account.deposit(200)
    account.withdraw(50)
    account.add_interest()
    account.show_transactions()
    print(account)

if __name__ == "__main__":
    main()