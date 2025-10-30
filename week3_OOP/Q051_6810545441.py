# Name: Krittitee Chaisang #  Student ID: 6810545441
class CoffeeMachine:
    def __init__(self, water, beans):
        self.__water_level = water
        self.__beans_level = beans
        
    def __grind_beans(self):
        self.__beans_level > 0
        return "Grinding coffee beans..."
    
    def __heat_water(self):
        self.__water_level > 0
        return "Heating water..."
    
    def __pour_espresso(self):
        return "Pouring espresso shot..."
    
    def make_espresso(self):
        if self.__beans_level > 10 and self.__water_level > 20:
            print(self.__heat_water())
            print(self.__grind_beans())
            print(self.__pour_espresso())
            return "Your espresso is ready!"
        else:
            return "Error: Please refill water or beans."
        
    def get_status(self):
        return f"Water: {self.__water_level}, Beans: {self.__beans_level}"
    
water = int(input("Enter initial water level: "))
beans = int(input("Enter initial beans level: "))
pluem = CoffeeMachine(water,beans)
while True:
    cmd = input("Enter command (make/status/exit): ")
    if cmd == 'make':
        print(pluem.make_espresso())
    elif cmd == 'status':
        print(pluem.get_status())
    elif cmd == 'exit':
        print("Goodbye.")
        break
    