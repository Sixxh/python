# faca um programa que tenha uma lista chamada numeros e duas funcoes chamadas sorteio() e somapar().
# a primeira funcao vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda funcao vai mostrar a soma entre todos os valores pares. sorteados pela funcao anterior.
from random import randint
from time import sleep
numeros = list()

def sorteia(list):
    cont = 0
    print('Sorteando 5 valores da lista: ', end='')
    while cont < 5:
        rands = randint(0, 10)
        list.append(rands)
        cont += 1
        sleep(0.3)
        print(rands, end=' ', flush=True)

def somapar(list):
    soma = 0
    for c in list:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {list}, temos {soma}')

sorteia(numeros)
print()
somapar(numeros)