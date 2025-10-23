# Name: Krittitee Chaisang # Student ID: 6810545441
x = list(map(int ,input("Enter three integers: ").split()))
summa = sum(x)

if summa == 0 : y = "Zero"
elif summa % 2 == 0: y = "Even"
else: y = "Odd" 
   
print(f"Sum: {y}")
print(f"Max: {max(x)}")
print(f"Min: {min(x)}")
