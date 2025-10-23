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
        
vehicle = []
while True:       
    input_ = input("Register (car/motorcycle): ")
    if input_ == 'car':
        brand = input("Enter brand: ")
        year = input("Enter year: ")
        num_doors = input("Enter number of doors: ")
        car = Car(brand, year, num_doors)
        print("Vehicle added.")
        vehicle.append(brand)
    elif input_ == 'motorcycle':
        brand = input("Enter brand: ")
        year = input("Enter year: ")
        has_sidecar = input("Has sidecar (True/False): ")
        mtb = Motorcycle(brand, year, has_sidecar)
        print(f"Vehicle added.")
        vehicle.append(brand)
    elif input_ == 'done':
        print('--- Registered Vehicles ---')
        for i in vehicle:
            print(i)
        break

while True:
    cmd = input("Enter command: ").split()
    try:
        action = cmd[0]
        brand_ = cmd[1]
        speed = int(cmd[2])
    except ValueError:
        print("Invalid command.")
    if action == 'accel' and brand_ != None and speed != None:
        print(f"{brand_} accelerates.")
        print(f"Status: Ford Speed: {speed}")
    elif action == 'accel' and brand_ == None and speed != None:
        print("Invalid command.")
    elif action == 'accel' and brand_ not in vehicle and speed != None:
        print("Vehicle not found.")
    elif action != 'accel' and brand_ != None and speed != None:
        print("Invalid command.")
    elif 