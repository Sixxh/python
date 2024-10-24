# crie um programa com uma tupla unica com nomes de produtos e seus respectivos precos na sequencia.
# no  final mostre uma listagem de precos, organizando os dados em forma tabular.
# listagem = ('Pao', 1, 'Leite', 3.50, 'Frango', 10.90)
# print('-' * 30)
# print(f'{'Listagem de preco':^30}')
# print('-' * 30)
# lista = listagem
# print(f'{lista[0]:.<21}', end='')
# print(f'R$ {lista[1]:>5.2f}')

# print(f'{lista[2]:.<21}', end='')
# print(f'R$ {lista[3]:>5.2f}')

# print(f'{lista[4]:.<21}', end='')
# print(f'R$ {lista[5]:>5.2f}')
# print('-' * 30)
listagem = (str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: ')), str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: ')), str(input('Digite o nome do produto: ')), float(input('Digite o valor do produto: ')))
print('-' * 30)
print(f'{"LISTAGEM DE PRECOS":^30}')
print('-' * 30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 30)