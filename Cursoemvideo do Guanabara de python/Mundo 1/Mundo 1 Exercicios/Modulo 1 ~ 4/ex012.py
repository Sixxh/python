# faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto
#valor_produto = float(input('Digite valor do produto: '))
#desconto = valor_produto - (0.05 * valor_produto)
#print('O produto fica por R${:.2f} com 5% de desconto.'.format(desconto))
#professor
preco = float(input('Qual o preco do produto: '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promocao com descondo de 5% vai custar R${:.2f}'.format(preco, novo))