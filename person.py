import enum

class Gender(enum.Enum):
    Male = 'male'
    Female = 'female'


class Person:

    def __init__(self, age: int, weight: float, height: float, gender: Gender):        
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender


    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    

    def calories(self) -> float:
        if self.gender == Gender.Male:
            return round((10 * self.weight) + (625 * self.height) - (5 * self.age) + 5, 2)
        else:
            return round((10 * self.weight) + (625 * self.height) - (5 * self.age) - 161, 2)


    def healthy_weight(self):
        return round(18.5 * (self.height ** 2), 2), round(24.9 * (self.height ** 2), 2)

    
    def ideal_weight(self) -> float:
        if self.gender == Gender.Male:
            if self.height <= 1.524:
                return 50
            else:
                return round(50 + (2.3 * ((self.height - 1.524) / 0.0254)), 2)
        else:
            if self.height <= 1.524:
                return 45.5
            else:
                return round(45.5 + (2.3 * ((self.height - 1.524) / 0.0254)), 2)

    
enoch = Person(24, 65, 1.6, Gender.Male)
print(enoch.calories())
print(enoch.bmi())
print(enoch.ideal_weight())
print(enoch.healthy_weight())