class Dog:
    # Class attribute
    species = "canis lupus familiaris"

    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age

    # Method
    def bark(self):
        return f'{self.name} says woof!'

class Puppy(Dog): # inheriting from dog class
    def __init__(self, name, age, training_level):
        super().__init__(name, age) # call the parent class constructor
        self.training_level = training_level

    def bark(self):
        return f'{self.name} says yip! (training level: {self.training_level})'

my_puppy = Puppy('Max', 1, 'Beginner')
print(my_puppy.bark())