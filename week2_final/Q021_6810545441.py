# Name: Krittitee Chaisang #  Student ID: 6810545441
from pathlib import Path

path = Path("greeting.txt")
name = input("Enter your name: ")

with open(path,"w")as f:
    f.write(f"Hello, {name}! Welcome to file handling.")
    
print(f"Greeting saved to {path}")
