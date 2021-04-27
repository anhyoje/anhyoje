class Human:
    def __init__(self, name, years, sex):
        self.name = name
        self.years = years
        self.sex = sex

A = Human("안효제", "28", "male")
print(A.name, A.years, A.sex)

class Level(Human):
    def __init__(self, **kwargs):
        super().__init__
        self.level = kwargs.get("level", "대리")

B = Level()
print(A.name, B.level)
