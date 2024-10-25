# faca um programaa que tenha uma funcao cahamda contador(). que receba tres paramentros: inicio, fim e passo e realize a contagem.
# seu programa tem que realizar tre contagens atraves da funcao criada.
# de 1 ate 10, de 1 em 1
# de 10 ate 0, de 2 em 2
# uma contagem personalizada.
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} ate o {f} de {p} em {p}.')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('\nFim!')
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('\nFim!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora e sua vez de personalizar a contagem.')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)