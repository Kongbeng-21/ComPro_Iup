# Name: Krittitee Chaisang # Student ID: 6810545441
s = int(input("Enter size of triangle: "))
p = input("Enter pattern string: ")

if s < 0 or p == "":
    print("Invalid input")
else:
    L = len(p)
    idx = 0
    for i in range(1, s + 1):
        line = []
        for _ in range(i):
            line.append(p[idx % L])
            idx += 1
        print("".join(line))
