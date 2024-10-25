class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f'{self.name} says Woof!'
    
class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def bark(self):
        return f'{self.name} the puppy says Woof!'
    
class Cat(Dog):
    def bark(self):
        return f'{self.name} says Meow'

my_cat = Cat('Whiskers', 'Siamese')
print(my_cat.bark())