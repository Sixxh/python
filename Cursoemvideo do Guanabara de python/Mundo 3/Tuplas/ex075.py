# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um atupla. no final mostre:
# quantas vezes apareceu o valor 9.
# em que posicao foi digitado o primeiro valor 3.
# quais foram os numeros pares
n = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
print(f'Voce digitou os valores {n}')
if 9 in n:
    print(f'O numero 9 apareceu {n.count(9)}')
else:
    print('O numero 9 nao foi digitado')
if 3 in n:
    print(f'O valor 3 foi digitado na posicao {n.index(3)+1}')
else:
    print('O numero 3 nao foi digitado')
print('Os Valores par digitados foram: ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')