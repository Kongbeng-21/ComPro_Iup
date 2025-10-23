from pathlib import Path
path = Path("journal.log")
while True:
    entry = input("Enter journal entry (or 'DONE' to exit): ")
    if entry == 'DONE':
        print("Journal closed.")
        break

    with open(path,"a")as f:
        f.write(entry + "\n")
        
    print("Entry saved.")