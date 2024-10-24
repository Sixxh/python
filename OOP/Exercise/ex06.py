class Animal:
    def make_sound(self):
        return 'Some Sound...'

class Dog(Animal):
    def make_sound(self):
        return 'Woof!'

class Cat(Animal):
    def make_sound(self):
        return 'Meow!'

class Cow(Animal):
    def make_sound(self):
        return 'Moo!'
    
# Programa Principal

dog = Dog()
print(dog.make_sound())

cat = Cat()
print(cat.make_sound())

cow = Cow()
print(cow.make_sound())