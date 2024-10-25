#escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a R$1250,00, calcule um aumento de 10%
#para inferiores ou iguais, o aumento e de 15%

#meu

#salario = float(input('Digite seu salario: '))
#if salario <= 1250:
#    print('Seu salario com aumento de 15% e {:.2f}'.format(salario * 1.15))
#else:
#    print('Seu salario com aumento de 10% e {:.2f}'.format(salario * 1.10))

#professor
salario = float(input('Digite seu salario: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu novo salario e R${:.2f}'.format(novo))