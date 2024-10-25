# crie um programa que leia o ano de nascimento de sete pessoass. No final, mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores
# maior idade = 21
from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(1, 8):
    nasc = int(input('Qual seu ano de nascimento? '))
    idade = ano - nasc
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('{} Pessoas tem mais de 21 anos.'.format(maior))
print('{} Pessoas tem menos de 21 anos.'.format(menor))