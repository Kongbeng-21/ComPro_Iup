# Name: Krittitee Chaisang # Student ID: 6810545441
rows = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))

mat = []
for i in range(rows):
    row = list(map(int,input(f"Enter row {i+1}: ").split()))
    mat.append(row)
   
print("\nTransposed Matrix:")

for j in range(col):
    line = []
    for i in range(rows):
        line.append(str(mat[i][j]))
    print(" ".join(line))
