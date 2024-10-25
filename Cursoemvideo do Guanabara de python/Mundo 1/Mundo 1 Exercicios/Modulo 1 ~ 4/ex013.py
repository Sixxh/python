# faca um algoritmo que leita o salario de um funcionario e mostre seu novo salario com 15% de aumento.
#salario = float(input('Qual seu salario: '))
#aumento = (0.15 * salario) + salario
#print('Voce recebeu um aumento de 15% de salario agora seu salario e: R${:.2f}'.format(aumento))
#professor
salario = float(input('Qual o salario do funcionaro? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, novo))
