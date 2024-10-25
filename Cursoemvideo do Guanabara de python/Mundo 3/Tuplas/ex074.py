from random import randint
maior = menor = 0
for c in range (5):
    nu = randint(1, 100)
    if c == 0:
        maior = nu
        menor = nu
        print('Os valores sorteados foram: ', end='')
    print(nu, end=' ')
    if nu > maior:
        maior = nu
    if nu < menor:
        menor = nu
print(f'\nO maior valor e: {maior}')
print(f'O menor valor e: {menor}')