# faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa
from math import hypot, sqrt
co = float(input('Comprimento Oposto: '))
ca = float(input('Comprimento Adjacent: '))
#hi = hypot(co, ca)
hi = sqrt(co ** 2 + ca ** 2) 
print('A hipotenusa e {:.2f}'.format(hi))