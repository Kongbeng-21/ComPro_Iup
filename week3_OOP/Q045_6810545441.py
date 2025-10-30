# Name: Krittitee Chaisang #  Student ID: 6810545441
class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
class Robot:
    def speak(self):
        return "BeepBoop!"

animal = ['dog','cat','robot']
while True:
    x = input("Create (dog/cat/robot/exit): ").lower()
    if x in animal:
        if x == 'dog':
            y = Dog()
            print(y.speak())
        if x == 'cat':
            y = Cat()
            print(y.speak())
        if x == 'robot':
            y = Robot()
            print(y.speak())
    if x == 'exit':
        print("Goodbye.")
        break