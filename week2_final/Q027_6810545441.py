# Name: Krittitee Chaisang #  Student ID: 6810545441
import csv 
from pathlib import Path

path = Path("inventory.csv")
category = input("Enter category to filter by: ").strip()
items = []
with open(path,"r",newline='')as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        item_id,item_name,cate,stock = row
        if cate.lower() == category.lower():
            items.append((item_name,stock))
            
if items:
    print(f"Items in category '{category}':")
    for item_name,stock in items:
        print(f"Item: {item_name}, Stock: {stock}") 
        
else:
    print(f"No items found in category '{category}'.")
    
        