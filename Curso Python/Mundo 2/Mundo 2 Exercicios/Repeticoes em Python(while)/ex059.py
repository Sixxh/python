# Crie um programa que leia dois valores e mostre um menu na tela
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos numeros
# [5] Sair do programa
# seu programa devera realizar a opeercao solicitada em cada caso.
menu = 0
while menu != 5 or menu == 4:
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print('''Qual Opcao Deseja?   
          [1] Somar
          [2] Multiplicar
          [3] Maior
          [4] Novos Numeros
          [5] Sair do programa''')
    menu = int(input('Escolha uma das opcoes: '))
    if menu == 1:
        soma = n1 + n2
        print('A soma entre {} e {} eh: {}'.format(n1, n2, soma))
    if menu == 2:
        mult = n1 * n2
        print('A multiplicacao entre {} e {} eh: {}'.format(n1, n2, mult))
    if menu == 3:
        maior = ''
        if n1 > n2:
            maior = 'Primeiro'
        if n2 > n1:
            maior = 'Segundo'
        print('O maior numero e o {}'.format(maior))