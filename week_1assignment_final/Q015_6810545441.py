# Name: Krittitee Chaisang # Student ID: 6810545441
import math

groups = {}

while True:
    line = input("Enter group name and coordinates (x y z) or 'done' to finish: ")
    if line == "done":
        break
    name, x, y, z = line.split()
    groups[name] = (float(x), float(y), float(z))

pairs = []

names = list(groups.keys())
for i in range(len(names)):
    for j in range(i+1, len(names)):
        g1, g2 = names[i], names[j]
        x1, y1, z1 = groups[g1]
        x2, y2, z2 = groups[g2]
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        pair_name = tuple(sorted([g1, g2]))   # จัดเรียงชื่อให้ออก 'A to B' ไม่ซ้ำ
        pairs.append((pair_name[0], pair_name[1], d))

pairs.sort(key=lambda x: x[2])

print("\nTop minimum distance pairs (show only top-5):")
for i, (g1, g2, d) in enumerate(pairs[:5], start=1):
    print(f"{i}. {g1} to {g2}: {d:.2f}")
