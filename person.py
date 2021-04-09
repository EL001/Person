class Person:

    def __init__(self, age: int, weight: float, height: float, gender: type):        
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        

    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
        

    def calories(self) -> float:
        if self.gender == 'male':
            return round((10 * self.weight) + (625 * self.height) - (5 * self.age) + 5, 2)
        else:
            if self.gender == 'female':
                return round((10 * self.weight) + (625 * self.height) - (5 * self.age) - 161, 2)


    def healthy_weight(self) -> float:
        return round(18.5 * (self.height ** 2), 2), round(24.9 * (self.height ** 2), 2)

    
    def ideal_weight(self) -> float:
        if self.gender == 'male':
            if self.height <= 1.524:
                return 50
            else:
                return round(50 + (2.3 * ((self.height - 1.524) / 0.0254)), 2)
        else:
            if gender == 'female':
                if self.height <= 1.524:
                    return 45.5
                else:
                    return round(45.5 + (2.3 * ((self.height - 1.524) / 0.0254)), 2)
    
    
enoch = Person(26, 65, 1.84, 'male')


person = 'Enoch'
cal = (enoch.calories())
bmi = (enoch.bmi())
ideal_w = (enoch.ideal_weight())
healthy_w = (enoch.healthy_weight())


print ( 'For a person named {}, the body mass index is {},'
         '\n''this indicates an ideal weight range of {}kg and a healthy weight of {}kg.'
           '\n''The minimum amount of the calories needed each when the body is at rest is {}kcal/day'
               .format(person, bmi, healthy_w, ideal_w, cal))