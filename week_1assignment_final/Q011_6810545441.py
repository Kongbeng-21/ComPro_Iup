# Name: Krittitee Chaisang
# Student ID: 6810545441

transaction_data_type = []
transaction_data_value = []

while True:
    transac_type = input("Enter transaction description (or 'done' to finish): ")
    if transac_type != "done":
        value = float(input(f"Enter amount for {transac_type}: "))
        if value > 0:
            transaction_data_type.append(transac_type)
            transaction_data_value.append(value)
        elif value < 0:
            transaction_data_type.append(transac_type)
            transaction_data_value.append(value)
        elif value == 0:
            pass
    elif transac_type == "done":
        break

print("\n--- FINANCIAL REPORT ---\nTransactions:")
for i in range(len(transaction_data_type)):
    if transaction_data_value[i] > 0:
        print(f"+ {transaction_data_type[i]+":":15}${transaction_data_value[i]:8.2f}")
    else:
        print(f"- {transaction_data_type[i]+":":15}${transaction_data_value[i]:8.2f}")

print("------------------------")

list_income = [j for j in transaction_data_value if j > 0]
list_expense = [k for k in transaction_data_value if k < 0]

print(f"{"Total Income:":17}${sum(list_income):8.2f}")
print(f"{"Total Expenses:":17}${sum(list_expense):8.2f}")
print(f"{"Net Balance:":17}${sum(transaction_data_value):8.2f}")

print("------------------------")