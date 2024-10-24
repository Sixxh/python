class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f'{self.name}, Salary: {self.salary}'
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f'{self.name}, Salary: {self.salary}, Department: {self.department}'
    
# Programa principal

emp = Employee('Alice', 50000)
print(emp.get_details())

mgr = Manager('Bob', 70000, 'HR')
print(mgr.get_details())