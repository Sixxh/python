# crie um programa com uma tupla unica com nomes de produtos e seus respectivos precos na sequencia.
# no  final mostre uma listagem de precos, organizando os dados em forma tabular.
listagem = ('Pao', 1, 'Leite', 3.50, 'Frango', 10.90)
print('-' * 30)
print(f'{"LISTAGEM DE PRECOS":^30}')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 30)