class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print('Digite um valor valido')
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsufficientFundsError('Voce nao tem saldo o suficiente')

    def check_balance(self):
        return f'Voce tem {self.__balance} disponivel na conta'



# Programa principal
account = BankAccount('Sixh', 10000)
account.deposit(100)
account.withdraw(10050)
print(account.check_balance())
