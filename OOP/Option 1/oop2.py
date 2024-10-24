class Cat:
    def __init__(self, name):
        self.__name = name # private attribute
    
    def get_name(self):
        return self.__name # public method to access the private attribute
    
my_cat = Cat('Whiskers')
print(my_cat.get_name())