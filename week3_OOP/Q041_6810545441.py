# Name: Krittitee Chaisang #  Student ID: 6810545441
student_id = (input("Enter student ID: "))
name = input("Enter name: ")
major = input("Enter major: ")

class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self._name = name
        self.__major = major
        self.credits = 0
        
    def get_info(self):
        return f"ID: {self.student_id}, Name: {self._name}, Major: {self.__major}, Credits: {self.credits}"
    
student_info = Student( student_id, name, major)
print(student_info.get_info())