# Crie um programa que leia dois valores e mostre um menu na tela
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos numeros
# [5] Sair do programa
# seu programa devera realizar a opeercao solicitada em cada caso.
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Qual numero e maior
    [4] Novos numeros
    [5] Sair do programa''')
    opcao = int(input('Qual a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('O resultado de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O resultado de {} x {} = {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor e {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte Sempre!')