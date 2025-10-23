def cal_cost(price ,quantity):
    return price * quantity

def show_price(orders):
    print("Order Summary:")
    total = 0
    for item ,price ,quantity in orders:
        cost = cal_cost(item ,price ,quantity)
        total += cost
        print(f"{item}: {quantity} x {price:.1f} = {cost:.1f} Baht")
    print(f"Total bill: {total:.1f} Baht")
   
orders = read_inputs()
show_price(orders
