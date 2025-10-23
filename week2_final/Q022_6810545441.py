# Name: Krittitee Chaisang #  Student ID: 6810545441
from pathlib import Path
 
name = input("Enter the filename to read: ")
path = Path(name)
print("Current working directory:", Path.cwd())
if path.exists():
    with open(path,"r")as f:
        print("--- File Content ---")
        content = f.read()
        print(content)
        print()
        words = content.split()
        print("--- Word Count ---")
        print(f"Total words: {len(words)}")

else:
    print(f"Error: The file '{name}' was not found.")
        