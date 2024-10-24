# crie um programa onde o usuario possa digitar varios alores numericos e cadastre-os em uma lista. caso o numero ja existal a dentro, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
listas = []
while True:
    num = int(input('Digite um numero: '))
    if num not in listas:
        listas.append(num)
    else:
        print('Numero ja esta na lista.')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
listas.sort()
print(listas)