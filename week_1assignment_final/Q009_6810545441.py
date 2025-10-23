# Name: Krittitee Chaisang # Student ID: 6810545441
items = int(input("How many items in inventory? "))
inventory = []
for i in range(items):
    print(f"\nItem {i+1}")
    while True:
        name = input("Enter name: ")
        same = [item["name"].lower() for item in inventory]
        if name.lower() in same:
            print("Invalid name, enter a different name")
        else:
            break
    price = float(input("Enter price: "))
    quantity = float(input("Enter quantity: "))
    subtotal = (price * quantity)
    data = {"name":name,
            "price":price,
            "quantity":quantity,
            "subtotal":subtotal} 
    inventory.append(data)
    
print("\nInventory Details:")
val = 0                 
for item in inventory:
    print(f"{item['name']} - Price: {item['price']:.2f}, Quantity: {item['quantity']:.0f}, Subtotal: {item['subtotal']:.2f}")
    val += item["subtotal"]
print()
print(f"Total inventory value: {val:.2f}")
