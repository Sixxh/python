# crie um programa que leia a idade e o sexo de varias pessoas. a acada pessoa cadastrada o programa devera perguntar se o usuario quer ou nao continuar no final mostre:
# a) quantas pessoas tem mais de 18 anos.
# b) quantos homens foram cadastrados
# c) quantas mulheres tem menos de 20 anos
maior18 = 0
homens_cadastrado = 0
mulheres_menor = 0
while True:
    nome = str(input('Qual seu Nome? '))
    idade = int(input('Qual sua Idade? '))
    sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo in 'M':
        homens_cadastrado += 1
    if sexo in 'F' and idade < 20:
        mulheres_menor += 1
    continuar = str(input('Deseja Cadastrar mais pessoas? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{maior18} pessoas sao maiores de 18 anos.')
print(f'Teve {homens_cadastrado} Homems Cadastrados.')
print(f'Teve {mulheres_menor} Mulheres menores de 20 anos.')