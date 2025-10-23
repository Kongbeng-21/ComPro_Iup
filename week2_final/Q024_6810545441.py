# Name: Krittitee Chaisang  # Student ID: 6810545441
f = open("scores.txt" , "r" , encoding = "utf-8")
score = f.read()
score = score.splitlines()

list = []
for sc in score:
    sc1 = sc.split(",")
    list.append(sc1)
top = ""
max = "0"

for n,m in list:
    current = m
    if current > max:
        max = current
        top = n

total = 0
avg = 0

for score in list:
    total += float(score[1])

avg = total / len(list)

print("--- Score Analysis ---")
print(f"Class Average: {avg:.2f}")
print(f"Highest Score: {top} with {max} points.")
