# a confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atelata e mostre sua categoria de acordo com a idade:
# ate 9 anos: mirim
# ate 14 anos: infaantil
# ate 19 anos: junior
# ate 20 anos: senior
# acima: master
from datetime import date
ano = int(input('Qual o ano do seu nascimento? '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria Mirim'.format(idade))
elif idade <= 14:
    print('Categoria Infantil'.format(idade))
elif idade <= 19:
    print('Categoria Junior'.format(idade))
elif idade <= 20:
    print('Categoria Senior'.format(idade))
elif idade > 20:
    print('Categoria Master'.format(idade))
else:
    print('Digite um ano valido ou voce esta muito novo para participar')