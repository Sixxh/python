#crie um porograma que leia um numero inteiro e mostre na tela se ele e par ou impar
n = int(input('Digite um numero: '))
if (n % 2) == 0:
    print('{} e Par'.format(n))
else:
    print('{} e Impar'.format(n))