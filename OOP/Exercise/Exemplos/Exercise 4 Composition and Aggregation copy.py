# Composition: A Car contains an Engine and controls its lifecycle.
# Aggregation: A Person uses a Car, but does not control its lifecycle.
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return 'Engine Started'
    
class Car:
    def __init__(self, engine):
        self.engine = engine # classe carro "possui(owns)" um motor (composition)

    def drive(self):
        return f'Driving with {self.engine.horsepower} horsepower engine'

class Person:
    def __init__(self, name):
        self.name = name

    def drive_car(self, car):
        return f'{self.name} is driving the car. {car.drive()}'

# Programa principal
engine = Engine(150)
car = Car(engine)
person = Person('John')

print(person.drive_car(car))