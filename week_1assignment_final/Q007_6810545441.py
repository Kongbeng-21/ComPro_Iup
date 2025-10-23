# Name: Krittitee Chaisang # Student ID: 6810545441
st = int(input("How many students? "))
grade = {}
for i in range(st):
    name = input(f"Enter name for student {i+1}: ")
    scores = list(map(float, input(f"Enter scores for {name}: ").split()))
    grade[name] = scores
    
print("\nStudent Averages:")
for name,scores in grade.items():
    avg = sum(scores) / len(scores)
    print(f"{name}: {avg:.2f}")
