# Name: Krittitee Chaisang #  Student ID: 6810545441
class Vehicle:
    def __init__(self, brand, year):
        self.brand : str = brand
        self.year : int = year
        self.speed = 0
        
    def accelerate(self, amount):
        if amount > 0:
            self.speed += amount
        return f"{self.brand} accelerates."
    
    def brake(self, amount):
        if amount > 0:
            self.speed -= amount
        return f"{self.brand} brakes"
    
    def get_status(self):
        return f"{self.brand} Speed: {self.speed}"
        
class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors : int = num_doors
        
class Motorcycle(Vehicle): 
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar : bool = has_sidecar
        
vehicles = []
while True:       
    input_ = input("Register (car/motorcycle): ")
    if input_ == 'car':
        brand = input("Enter brand: ")
        year = int(input("Enter year: "))
        num_doors = input("Enter number of doors: ")
        car = Car(brand, year, num_doors)
        print("Vehicle added.")
        vehicles.append(car)
    elif input_ == 'motorcycle':
        brand = input("Enter brand: ")
        year = input("Enter year: ")
        has_sidecar = input("Has sidecar (True/False): ")
        mtb = Motorcycle(brand, year, has_sidecar)
        print(f"Vehicle added.")
        vehicles.append(mtb)
    elif input_ == 'done':
        print('--- Registered Vehicles ---')
        for i in vehicles:
            print(i.brand)
        print("---------------------------")
        break
        

while True:
    cmd = input("Enter command: ").split()
    if len(cmd) == 1 and cmd[0].lower() == 'exit':
        print('Goodbye.')
        break
    try:
        action = cmd[0]
        brand = cmd[1]
        speed = int(cmd[2])
    except ValueError and IndexError:
        print("Invalid command.")

    if action != "accel":
        print("Invalid command.")
        continue
    if len(cmd) != 3:
        print("Invalid command.")
        continue
    found = False
    for v in vehicles:
        if v.brand == brand:
            print(v.accelerate(speed))
            found = True
    if not found:
        print("Vehicle not found.")
        continue
    for v in vehicles:
        print(f"Status: {v.get_status()}")
    
    