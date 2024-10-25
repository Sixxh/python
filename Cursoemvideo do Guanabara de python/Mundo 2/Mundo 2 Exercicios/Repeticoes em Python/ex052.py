# faca um programa que leia um numero inteiro e diga se ele e um numero primo
# n = int(input('Digite um numero: '))
# if n < 2:
#    print('Nao Primo')
# elif n > 2:
#     for c in range(2, int(n/2)):
#         if n % c == 0:
#             print('Nao Primo')
# else:
#     print('Primo')

#professor 

n = int(input('Digite um numero: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {}'.format(n, tot))
if tot == 2:
    print('Ele e um numero primo')
else:
    print('Ele nao e um numero primo')