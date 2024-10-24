# faca um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0 com uma pausa de 1 segundo entre eles
# https://youtu.be/cL4YDtFnCt4?t=1271
from time import sleep
print('''Deseja estourar os fogos ?
[ 1 ] SIM
[ 2 ] NAO''')
contagem = int(input('Qual sua escolha ? '))
if contagem == 1:
    for c in range (10, 0, -1):
        print('O fogo de artifico ira estoura em {}'.format(c))
        sleep(1)
    print('KABOOMMMMM')
else:
    print('Voce escolheu opcao 2 e os fogos nao irao estourar')