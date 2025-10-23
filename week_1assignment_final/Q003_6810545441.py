# Name: Krittitee Chaisang # Student ID: 6810545441
n = int(input("Enter a non-negative integer: "))

def fac(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

if n == 0:
    print("Factorial Sum is: 0")
else:
    fact_sum = 0
    for i in range(1,n+1):
        fact_sum += fac(i)
    print("Factorial Sum is:", fact_sum)
        
