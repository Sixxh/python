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


my_dog = Puppy('Buddy', 'Golden Retriever', 1)
print(my_dog.bark())