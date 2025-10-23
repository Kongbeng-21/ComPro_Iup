# Name: Krittitee Chaisang # Student ID: 6810545441
s = input("Enter a string: ")

if s == "":
    print("Empty input")
else:
    s = s.lower()
    freq = {}
    for ch in s:
        if ch == " ":
            continue
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in freq:
        print(f"{ch}: {freq[ch]}")
