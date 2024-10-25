# crie um programa que tenhaa um tupla totalmente preechida com uma contagem por extenso, de zero ate vinte.
# seu programa devera ler um   numero pelo teclado (entre 0 e 20) e mostralo por extenso
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um numero entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Digite novamente, um numero entre 0 e 20: '))
print(f'Voce digitou o numero {cont[n]}')