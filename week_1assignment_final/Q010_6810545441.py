# Name: Krittitee Chaisang # Student ID: 6810545441
while True:
    s = input("Enter a sentence (or 'exit' to quit): ")
    if s.lower() == "exit":
        print("Goodbye!")
        break

    vowels = "aeiou"
    count = 0
    for ch in s.lower():  
        if ch in vowels:
            count += 1

    print(f"Vowels: {count}")