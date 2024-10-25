class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('Insufficient funds!')
        else:
            self.__balance -= amount

    def get_balance(self):
        return f'Mr. {self.owner}, your current balance is {self.__balance}'

# Programa principal
account = BankAccount('John Doe', 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())