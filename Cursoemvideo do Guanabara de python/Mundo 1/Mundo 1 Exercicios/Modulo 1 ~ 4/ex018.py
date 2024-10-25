# faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians
ang = float(input('Digite um angulo entre 0 e 360: '))
se = sin(radians(ang))
co = cos(radians(ang))
ta = tan(radians(ang))
print('O seno e {:.2f} o Cosseno e {:.2f} e a tangente {:.2f}'.format(se, co, ta))