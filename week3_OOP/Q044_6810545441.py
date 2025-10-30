# Name: Krittitee Chaisang #  Student ID: 6810545441
import math
class Shape:
    def __init__(self, color):
        self.color = color
        
    def get_area(self):
        return 0
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = int(radius)
    def get_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height
    
    def get_area(self):
        return 0.5 * self.base * self.height
    
    
shape = input("Create (circle/rectangle/triangle): ")
if shape == 'circle':
    color = input("Enter color: ")
    radius = float(input("Enter radius: "))
    c = Circle(color,radius)
    print(f"Info: Color: {c.color}, Area: {c.get_area():.2f}")
    
if shape == 'rectangle':
    color = input("Enter color: ")
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    r = Rectangle(color,width,height)
    print(f'Info: Color: {r.color}, Area: {r.get_area():.2f}') 
    
if shape == 'triangle':
    color = input("Enter color: ")
    base = int(input("Enter base: "))
    height = int(input("Enter height:"))
    t = Triangle(color,base,height)
    print(f"Info: Color: {t.color}, Area: {t.get_area():.2f}")
    

