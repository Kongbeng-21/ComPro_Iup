class Score:
    def __init__(self, name: str, score: float):
        self.name = name 
        self.score = score
        self.grade = None
    def calculate_grade(self) -> str :
        if self.score >= 90:
            self.grade = 'A'
        elif 80 < self.score < 90:
            self.grade = 'B'
        elif 70 < self.score < 80:
            self.grade = 'C'
        elif 60 < self.score < 70:
            self.grade = 'D'
        else:
            self.grade = 'F'
        return self.grade
    
    def get_info(self) -> str:
        return f'Name: {self.name}, Score: {self.score:.2f}, Grade: {self.grade}'
    
name = input('Enter name: ')
score = float(input('Enter score: '))
if 0 > score > 100:
    print("Invalid score.")
sc = Score(name,score)
print(sc.get_info())