import math
class Shape:
    def __init__(self, shape_type: str, size: float, name: str) -> None:
        self.shape_type = shape_type
        self.size = size
        self.name = name
        
    def area(self) -> float :
        if self.shape_type == 'Square'.upper():
            area = self.size ** 2
        elif self.shape_type == 'Circle'.upper():
            area = math.pi * (self.shape_type ** 2)
        elif self.shape_type == 'Triangle'.upper():
            area = (math.sqrt(3)/4) * (self.size**2)
        return area
    
    def get_info(self,area) -> str:
        return f'Shape: {self.shape_type}, Size: {self.size}, Area: {area}, Name: {self.name}'
    
    def get_name(self) -> str:
        return self.name.upper()

shape_list = []
shpe = ['square', 'circle', 'triangle']
while True:
    shape_type = input('Enter shape type: ')
    if shape_type == 'done':
        print("-----REPORT-----")
        if len(shape_list)>0:
            print(shape.get_info())
        else:
            print('No shapes recorded')
        break
    shape_list.append(shape_type)
    size = float(input('Enter size: '))
    shape_list.append(size)
    name = input('Enter name: ')
    shape_list.append(name)
    shape = Shape(shape_type, size, name)
    
    