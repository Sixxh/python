class InsufficientFundsError(Exception):
    pass

class InvalidDepositError(Exception):
    pass

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise InvalidDepositError('O valor depositado deve ser positivo.')
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            raise InsufficientFundsError('Voce nao tem saldo o suficiente')

    def check_balance(self):
        return f'Voce tem {self.__balance} disponivel na conta'



# Programa principal
try:
    account = BankAccount('Sixh', 10000)
    account.deposit(1000)
    account.withdraw(500)
except InsufficientFundsError as e:
    print(f'Erro: {e}')
except InvalidDepositError as e:
    print(f'Erro: {e}')
else:
    print(account.check_balance())
finally:
    print('Operacao bancaria finalizada')