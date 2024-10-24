# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
# o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.
casa = float(input('Qual o valor da casa?? '))
salario = float(input('Qual seu salario?? '))
anos = int(input('Em quantos anos voce quer pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado')