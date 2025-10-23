# Name: Krittitee Chaisang #  Student ID: 6810545441
class Vehicle:
    def __init__(self, brand, year):
        self.brand : str = brand
        self.year : int = year
        
class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        super().__init__(brand, year)
        self.num_doors : int = num_doors
        
class Motorcycle(Vehicle): 
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar : bool = has_sidecar
        
input_ = input("Register (car/motorcycle): ")
if input_ == 'car':
    brand = input("Enter brand: ")
    year = input("Enter year: ")
    num_doors = input("Enter number of doors: ")
    car = Car(brand, year, num_doors)
    print(f"Registered: Brand: {car.brand}, Year: {car.year}, Doors: {car.num_doors}")
elif input_ == 'motorcycle':
    brand = input("Enter brand: ")
    year = input("Enter year: ")
    has_sidecar = input("Has sidecar (True/False): ")
    mtb = Motorcycle(brand, year, has_sidecar)
    print(f"Registered: Brand: {mtb.brand}, Year: {mtb.year}, Sidecar: {mtb.has_sidecar}")
