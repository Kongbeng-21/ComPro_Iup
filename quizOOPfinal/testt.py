score = 90
class Score:
    def __init__(self, name: str, score: float):
        self.name = name 
        self.score = score
        
    def calculate_grade(self) -> str :
        if self.score >= 90:
            self.grade == 'A'
        elif 80 < self.score < 90:
            self.grade == 'B'
        elif 70 < self.score < 80:
            self.grade == 'C'
        elif 60 < self.score < 70:
            self.grade == 'D'
        else:
            self.grade == 'F'
        return self.grade