class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce (self):
        print(f"My name is {self.name} I am {self.age} years old, and am a {self.gender}")
person = Person("Eugene", 20, "Male")

person.introduce()      
