class Student:
    #Constructors
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def study(self):
        print(f"{self.name} is studying {self.age} years")

    def play(self):
        print(f"{self.name} is playing {self.age} years")

s1 = Student("Bhargav", 22, 75)
print(f"Name:{s1.name}\nAge:{s1.age}\nMarks:{s1.marks}")
s2 = Student("Mohith", 20, 85.6)
print(f"Name:{s2.name}\nAge:{s2.age}\nMarks:{s2.marks}")

print(s1.name)
print(s1.age)
print(s1.marks)

s1.study()
s1.play()