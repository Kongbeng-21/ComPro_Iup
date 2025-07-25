Category = []
Amount = []


while True:
    print('=' * 20)
    print("EXPENSE TRACKER MENU ")
    print('=' * 20)
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View by Category")
    print("4. Spending Summary")
    print("5. Exit ")

    x = int(input("Enter your choice (1-5): "))

    if x == 1:
        y = float(input("Enter amount: "))
        z = input("Enter category (food, transport, entertainment, shopping, bills): ")
        Category.append(z)
        Amount.append(y)

    elif x == 2:
        print('=== ALL EXPENSE ===')
        print('Category           Amount')
        print('-' * 20)
        total = 0
        for i in range(len(Category)):
            print(f'{Category[i]:<18} {Amount[i]:.2f}')
            total += Amount[i]
        print('-' * 20)
        print(f"Total:             {total:.2f}\n")
        
    elif x==3:
        search = input("Enter Category to filter by: ")
        print('=== EXPENSE FOR "{search}"  ===')
        print('Category           Amount')
        print('-'*20)
        found=False
        total=0
        for i in range(len(Category)):
            if Category[i].lower() == search.lower():
                print(f'{Category[i]:<18} {Amount[i]:.2f}')
                total += Amount[i]
                found = True
        if found:
            print('-' * 30)
            print(f"Total:             {total:.2f}\n")
        else:
            print("No expense in that category.\n")
            
    elif x==4:
        print('=== SPENDING SUMMARY ===')
        summary={}
        total=0
        for i in range(len(Category)):
            cat=Category[i]
            amt=Amount[i]
            summary[cat] = summary.get(cat, 0) + amt
            total += amt
        for can in summary:
            percent = (summary[can] / total)*100
            print(f'{can:<18}: {summary[can]:.2f} ({percent:.2f}%)')
        print(f'Total:    {total:.2f}\n')
        
        
    
    else :
        print('Exit from the menu: ')
        break
        
        
        
            


