# Name: Krittitee Chaisang # Student ID: 6810545441
import math

print("Enter coefficients for f(x) = ax^2 + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("\nEnter coefficients for g(x) = dx^2 + ex + f")
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))

print()
start = float(input("Enter the start of the interval (a): "))
end = float(input("Enter the end of the interval (b): "))
n = int(input("Enter the number of trapezoids (n): "))

if start >= end:
    print("Error: The start of the interval must be less than the end.")
    exit()
if n <= 0:
    print("Error: The number of trapezoids must be a positive integer.")
    exit()

dx = (end - start) / n

def f1(x):
    return a * x**2 + b * x + c

def f2(x):
    return d * x**2 + e * x + f

area = 0
for i in range(n):
    x_i = start + i * dx
    x_next = start + (i + 1) * dx
    y1 = abs(f1(x_i) - f2(x_i))
    y2 = abs(f1(x_next) - f2(x_next))
    area += (y1 + y2) / 2 * dx

print(f"\nApproximate area: {area:.6f}")
