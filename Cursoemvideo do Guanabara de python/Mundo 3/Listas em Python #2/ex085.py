# crie um programa onde o usuario possa digitar sete valores numericos e cadastre-osem uma lista unica que mantenha separados os valores pares e impares. no final, mostre os valores pares e impares em ordem crescente.
geral = []
par = []
impar = []
for n in range(0, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
       par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
geral.append(par[:])
geral.append(impar[:])
print('-=' * 30)
print(f'Os valores pares digitados foram: {geral[0]}')
print(f'Os valores impares digitados foram: {geral[1]}')