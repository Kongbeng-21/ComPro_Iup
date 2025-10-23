# Name: Krittitee Chaisang #  Student ID: 6810545441
class Motorcycle:
    def __init__(self):
        self.speed = 0
        self.mileage = 0
    
    def start(self):
        return "Motorcycle is starting..."
    
    def accelerate(self, amount):
        self.speed += amount
        return f"Accelerating... Current speed: {self.speed} km/h"
    
    def add_mileage(self, distance):
        self.mileage += distance
    
    def stop(self):
        self.speed = 0
        return "Motorcycle has stopped."
    
    def get_status(self):
        return f"Current Speed: {self.speed} km/h, TotalMileage: {self.mileage} km"

bike = Motorcycle()
while True:
    cmd = input("Enter command: ").split()
    try:
        action = cmd[0]
        move = int(cmd[1])
    except IndexError or ValueError:
        move = None
        
    if action in ['start','accel','mileage','stop','status','exit']:   
        if action == 'exit': 
            print("Goodbye.")
            break
        elif action == 'start' and move == None:
            print(bike.start())
        elif action == 'accel' and move != None:
            print(bike.accelerate(move))
        elif action == 'mileage' and move != None:
            bike.add_mileage(move)
        elif action == 'stop' and move == None:
            print(bike.stop())
        elif action == 'status' and move == None:
            print(bike.get_status())
        else:
            print("Invalid command. Please try again.")
    else:
        print('Invalid command. Please try again.')
        

