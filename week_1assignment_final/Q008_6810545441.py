# Name: Krittitee Chaisang # Student ID: 6810545441
N = int(input("Enter table size: "))

if N <= 0:
    print("Invalid input")
else:
    for i in range(1, N + 1):       
        for j in range(1, N + 1):   
            print(f"{i*j:4}", end="")   
        print()  