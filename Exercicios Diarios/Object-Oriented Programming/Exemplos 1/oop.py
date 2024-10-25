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
    
# creating an object

my_dog = Dog("buddy", 3)
print(my_dog.bark()) # output: buddy says woof!