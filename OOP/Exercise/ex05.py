class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return print(f'Hello, my name is {self.name}')

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def greet(self):
        return print(f"Hello, my name is {self.name}, and I'm majoring in {self.major}")
    

# Programa Principal

person = Person('John', 30)
person.greet()

student = Student('Emily', 21, 'S12345', 'Computer Science')
student.greet()