#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porcao inteira
#ex: digite um numero: 6.127 "o numero 6.127 tem a parte inteira 6"
from math import trunc
num = float(input('Digite um numero: '))
real = trunc(num)
print('O numero {} tem a parte inteira {}'.format(num, real))