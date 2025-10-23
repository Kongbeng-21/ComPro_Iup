# Name: Krittitee Chaisang # Student ID: 6810545441
size = int(input("Enter an odd number for the size: "))

if size <= 0 or size % 2 == 0:
    print("Error: Please enter a positive odd number.")
else:
    char = input("Enter the character to use: ")
    mid = size //2
        
    for i in range(mid):
        space = abs(mid-i)
        inner = size - 2 * space -2
        print(" " * space + char + (" " * inner + char if i != 0 else " "))
        
    print(char*size)
    
    for i in range(mid -1,-1,-1):
        space = abs(mid-i)
        inner = size - 2 * space -2
        print(" " * space + char + (" " * inner + char if i != 0 else " "))
        
        

