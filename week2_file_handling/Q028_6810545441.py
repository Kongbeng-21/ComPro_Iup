# Name: Krittitee Chaisang #  Student ID: 6810545441
import csv
from pathlib import Path

path = Path("sales.tsv")

totals = {}
with open(path,"r")as f:
    reader = csv.reader(f,delimiter="\t")
    next(reader)
    for row in reader:
        reg,prod,sales = row
        sales = float(sales)
        if reg not in totals:
            totals[reg] = 0
        totals[reg] += sales 
        
print("--- Regional Sales Summary ---")
for reg ,total in totals.items():
    print(f"{reg}: ${total:.2f}")