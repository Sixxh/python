#  crie um programa que leia o nome e o preco de varios produtos. o programa devera perguntar se o usuario vai continuar. no final mostre:
# a) qual e o total gasto na compra
# b) quantos produtos custam mais de 1000
# c) qual e o nome do produto mais barato
barato_nome = ''
valor_barato = total_gasto = maisdemil = 0
while True:
    produto_nome = str(input('Qual o nome do produto? '))
    produto_valor = float(input('Qual o valor do produto? R$'))
    continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    total_gasto += produto_valor
    if valor_barato == 0:
        valor_barato = produto_valor
    if valor_barato > produto_valor:
        valor_barato = produto_valor
        barato_nome = produto_nome
    if produto_valor >= 1000:
        maisdemil += 1
    if continuar in 'N':
        break
print(f'O total gasto foi R${total_gasto:.2f}')
print(f'{maisdemil} produtos custam mais de R$1000,00 reais')
print(f'O produto mais barato foi {barato_nome}')