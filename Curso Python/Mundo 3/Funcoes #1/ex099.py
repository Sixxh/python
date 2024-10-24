# faca um programa que receba uma funcao chamada maior(), que receba varios parametros com valores inteiros.
# seu programa tem que analisar todos os valores e dizer qual deles e o maior.
from time import sleep
def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(1)
    tam = len(num)
    for c, v in enumerate(num):
        print(v, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {tam} valores ao todo.')
    sleep(0.5)
    maior = num[0]
    for c, v in enumerate(num):
        if maior < v:
            maior = v
    sleep(0.5)
    print(f'O maior valor informado foi {maior}')


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
#maior() < n funciona dessa forma