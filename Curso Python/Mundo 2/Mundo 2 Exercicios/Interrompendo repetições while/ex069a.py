# crie um programa que leia a idade e o sexo de varias pessoas. a acada pessoa cadastrada o programa devera perguntar se o usuario quer ou nao continuar no final mostre:
# a) quantas pessoas tem mais de 18 anos.
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos
tot18 = toth = totm20 = 0
while True:
    idade = int(input('Qual sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('Acabou')
print(f'{tot18} pessoas tem mais de 18 anos.')
print(f'{toth} Homens cadastrados.')
print(f'{totm20} Mulheres tem menos de 20 anos.')