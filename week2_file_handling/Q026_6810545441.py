# Name: Krittitee Chaisang #  Student ID: 6810545441
# Name: Krittitee Chaisang  # Student ID: 6810545441
import csv
from pathlib import Path

path = Path("contacts.csv")

with open(path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Phone"])

    i = 1
    while True:
        print(f"--- Enter Contact {i} ---")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        writer.writerow([name, email, phone])

        another = input("Add another contact? (yes/no): ").strip().lower()
        if another == "no":
            break

        print()
        i += 1

print(f"\nContact list saved to {path}.")
