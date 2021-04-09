class Person(builtins.object)
   
   
   Person(age: int, weight: float, height: float, gender: type)
   
   This class collects parameters; age, weight, height and gender for any person
   and contains methods which returns the bmi, kcal used per day, ideal weight range using the bmi and healthy weight for any person
   
   Methods defined here:
   
   __init__(self, age, weight, height, gender)
      
      Parameters
      ----------
       age : int
           Age of person
       weight : float
           Weight of person in kilograms
       height: float
           Height of person in metres
       gender: str
           Gender of person either male or female 
   
   
   bmi(self) -> float
       
       Returns the Body Mass Index (BMI) ratio of this person.
       BMI is calculated as weight divided by the square of the height.
       Weight and height are given in kg and m respectively.
       
   
   calories(self) -> float
       
       Returns the kcal/day which indicates the basal metabolic rate(BMR).
       BMR is the minimum amount of calories the body needs when at rest.
       Using Mifflin-St Jeor Equation:
       male:
           BMR = (10 * weight) + (625 * height) - (5 * age) + 5
       female:
           BMR = (10 * weight) + (625 * height) - (5 * age) - 161
   
   
   
   healthy_weight(self) -> float
       
       Returns the healthy weight limits using the bmi values recommended for maintaining a healhty weight                 
   
   
   
   ideal_weight(self) -> float
       
       Returns the ideal weight of this person.
       Using B.J Devine Formular;
       If height is less than 1.524m, the program returns an ideal weight of 50kg for males, while for females it returns 45.5kg. 
       If person is taller than 1.524m, the height is calculated as follows
       male:
       50 + (2.3 * ((height - 1.524) / 0.0254))
       
       female: 
       if height is less than 1.524m then the program returns an ideal weight of 45.5kg. If person is taller than 1.524m ,
       the height is calculated as follows
       45.5 + (2.3 * ((height - 1.524) / 0.0254))
