# Name: Krittitee Chaisang #  Student ID: 6810545441
class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self._name = name
        self.__major = major
        self.credits = 0
        
    def get_info(self):
        return f"ID: {self.student_id}, Name: {self._name}, Major: {self.__major}, Credits: {self.credits}"
    
    def complete_course(self, course_credits):
        if course_credits > 0:
            self.credits += course_credits
        return None
    
student_id = input("Enter student ID: ")
name = input("Enter name: ")
major = input("Enter major: ")
print("---")
pluem = Student(student_id, name, major)
while True:
    credits = input("Enter credits (or 'done'): ")
    if credits == 'done':
        break
    else:
        credits = int(credits)
        pluem.complete_course(credits)      
print(pluem.get_info())