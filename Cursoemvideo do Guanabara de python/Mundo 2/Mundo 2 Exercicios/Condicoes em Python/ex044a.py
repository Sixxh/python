# elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
# a vista dinheiro/chque: 10% desconto
# a vista no cartao: 5% de desconto
# em ate 2x no cartao: preco normal
# 3x ou mais no cartao: 20% de juros
print('{:=^40}'.format(' Lojas Sixh '))
preco = float(input('Qual o valor do produto? R$ '))
print('''Formas de pagamento.
1. A vista dinheiro/cheque: 10% de desconto.
2. A vista no cartao: 5% de desconto.
3. Em ate 2x no cartao: sem jusos/desconto.
4. 3x ou mais no cartao: 20% de juros.''')
forma = int(input('Qual a forma de pagamento ? '))
if forma == 1:
    total = preco - (preco * 10 / 100)
elif forma == 2:
    total = preco - (preco * 5 / 100)
elif forma == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parecela em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif forma == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas vao ser? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} com 20% de juros.'.format(totparc, parcela))
else:
    print('Escolha uma opcao valida.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))