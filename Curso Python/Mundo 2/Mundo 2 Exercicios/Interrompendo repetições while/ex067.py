# faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. o programa sera interrompido quando o numero solicitado for negativo.
n2 = 0
mult = 0
repet = 10
n = int(input('Digite um numero que deseja ver a tabuada: '))
while True:
    if repet == 0:
        n = int(input('Digite um numero que deseja ver a tabuada: '))
        repet += 10
        n2 = 0
    if n < 0:
        break
    n2 += 1
    mult = n*n2
    print(f'{n} x {n2} = {mult}')
    repet -= 1
print('Fim')