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
    calc = preco - (preco * 10 / 100)
    print('O valor do produto eh R${:.2f} com 10% de desconto.'.format(calc))
elif forma == 2:
    calc = preco - (preco * 5 / 100)
    print('O valor do produto eh R${:.2f} com 5% de desconto.'.format(calc))
elif forma == 3:
    calc = preco / 2
    print('O valor do produro eh R${:.2f} dividindo em 2x no cartao que fica 2x de R${:.2f}.'.format(preco, calc))
elif forma == 4:
    juros = preco + (preco * 20 / 100)
    calc = juros / 3
    print('O valor do produto eh R${:.2f} dividindo em 3x no cartao fica com juros de 20% e o valor e de 3x de R${:.2f}.'.format(preco, calc))