# faca um programa que leia um numero qualquer e mostre o seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120
# fazer com while e dps tentar fazer com for e dps com os 2

# usando while

# n = int(input('Digite um numero: '))
# para = n
# mult = n
# valor = 0
# while para != 1:
#     n -= 1
#     valor = mult
#     mult *= n
#     para -= 1
#     print('{} x {} = {}'.format(valor, n, mult), end=' / ')

# Usando while e for

# n = int(input('Digite um numero: '))
# para = n
# mult = n
# valor = 0
# c = 0
# while c != para:
#     for c in range(1, para):
#         c += 1
#         n -= 1
#         valor = mult
#         mult *= n
#         print('{} x {} = {}'.format(valor, n, mult), end=' / ')

# usando for 

n = int(input('Digite um numero: '))
para = n
mult = n
valor = 0
for c in range(1, para):
    n -= 1
    valor = mult
    mult *= n
    print('{} x {} = {}'.format(valor, n, mult), end=' / ')