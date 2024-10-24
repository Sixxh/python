# crie um programa onde o usuario possa digitar varios alores numericos e cadastre-os em uma lista. caso o numero ja existal a dentro, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print('-=' * 30)
print(f'Voce digitou os valores {numeros}')