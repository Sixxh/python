# desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o
# s = 0
# for c in range(6):
#     n = int(input('Digite um numero: '))
#     if (n % 2) == 0:
#        s = s + n
# print('A some entre os numeros pares e {}'.format(s))

# professor
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Voce informou {} numeros e a some foi {}.'.format(cont, soma))
