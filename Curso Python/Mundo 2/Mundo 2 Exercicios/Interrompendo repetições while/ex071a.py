# crie um programa que simule o funcionamento de um caixa eleetronico. no inicio, pergunte ao usuario qual ser ao valor a ser sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# obs: considere que o caixa possui cedulas de 50, 20, 10 e 1
print('=' * 30)
print('{:^30}'.format('Banco CEV'))
print('=' * 30)
valor = int(input('Qual valor deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)