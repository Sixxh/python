# faca um programa que leia um numero qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120
# fazer com while e dps tentar fazer com for e dps com os 2
n = int(input('Digite um numero para calcular seu factorial: '))
c = n
f = 1
print('Calculado {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))