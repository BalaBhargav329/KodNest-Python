class Student:
    # class attr - classname or obj ref
    company = "kodenst Technologoes"
    # Constructor
    def __init__(self, name, age):
        # Instance attributes - self or obj ref
        self.name = name
        self. age = age

    # Instance method - using self reference, obj ref
    def study(self):
        a = 10 # Local attribute
        print(a)
        print(f"{self.name} is studying")

    # Instance methods
    def getDetails(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Company:", self.company)

    # static methods - classname , objref
    @staticmethod    
    def trip(name):
        print(f"{name} goes for a trip")

    # class methods - classname , objref
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

Student.change_company("kodnest Technologies pvt lmt")
s1 = Student("Bhargav", 22)
print(Student.company)
print(s1.company)
print(s1.name)
s1.study()
s1.getDetails()

print("\n")
s2 = Student("Priya", 21)
Student.trip(s2.name)
print(s2.name)
s2.study()
s2.getDetails()

    