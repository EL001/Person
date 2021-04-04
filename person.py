class Person():
    def __init__ (self):
        self.height = int(input("Input height in cm"))
        self.weight = int(input("Input weight in kg"))
        self.age = int(input("Input age"))

        
    def BMI(self):
        height = self.height
        weight = self.weight

        BMI = weight / (height/100)**2

        if BMI <= 18.4:
            print("You are underweight.")
        elif BMI <= 24.9:
            print("You are healthy.")
        elif BMI <= 29.9:
            print("You are over weight.")
        elif BMI <= 34.9:
            print("You are severely over weight.")
        elif BMI <= 39.9:
            print("You are obese.")
        else:
            print("You are severely obese.")


el = Person()
el.BMI()


