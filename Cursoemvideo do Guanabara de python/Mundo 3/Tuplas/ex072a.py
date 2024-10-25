# crie um programa que tenhaa um tupla totalmente preechida com uma contagem por extenso, de zero ate vinte.
# seu programa devera ler um   numero pelo teclado (entre 0 e 20) e mostralo por extenso
cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Voce digitou o numero {cont[n]}')