#desenvolva um programa que leia o comprimento de tres retos e diga ao usuario se elas podem ou nao formar um triangulo
# https://youtu.be/K10u3XIf1-Q?t=1910
a = float(input('Digite comprimento base: '))
b = float(input('Digite comprimento esquerdo: '))
c = float(input('Digite comprimento direito: '))
if (b - c < a) and (a < b + c):
    print('Voce pode formar um triangulo')
else:
    print('Voce nao pode formar um triangulo')