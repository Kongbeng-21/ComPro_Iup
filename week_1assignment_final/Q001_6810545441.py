# Name: Krittitee Chaisang # Student ID: 6810545441
b,h = map(float, input("Enter base and height: ").split())
if b < 0 or h < 0:
    print("Input incorrect")
else:
    area = 0.5 * b * h
    print(f"Area: {area:.2f}")


