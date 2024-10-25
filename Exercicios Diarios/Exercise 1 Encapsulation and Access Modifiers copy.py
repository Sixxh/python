class Account:
    def __init__(self, owner, balance):
        self.__balance = balance
        self._owner = owner
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print('Voce nao tem essa quantia em dinheiro para saque')

    def get_balance(self):
        return f'{self.__balance}'
    
account = Account('John Doe', 1000)
account.deposit(500)
print(account.get_balance())
account.withdraw(200)
print(account.get_balance())

print(account._owner) # com apenas um _ consegue ser acessado fora da class mas e tratado como semi-privado, pode ser acessado mas n modificado a nao ser que seja necessario
# print(account.__balance) ## nao pode ser acessado fora da classe, isso faz parte de encapsulation (esconder estado atual do objeto para prevenir acesso nao autorizado.) so pode ser acessado via get metodos como get_balance por exemplo