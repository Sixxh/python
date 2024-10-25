# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
# A media de idade do grupo.
# qual e o nome do homem mais velho.
# quantas mulheres tem menos de 20 anos.
mulheres = 0
velho = 0
nome_velho = ''
idade2 = 0
for c in range (1, 5):
    nome = str(input('Qual seu nome: ')).lower()
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu genero: ')).lower()
    idade2 += idade
    if c == 0 and sexo == 'm':
        velho = idade
    else:
        if sexo == 'm' and idade > velho:
            velho = idade
            nome_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres += 1
print('O homem mais velho e {}'.format(nome_velho))
print('Tem {} mulheres menores de 20 anos'.format(mulheres))
media = idade2 / 4
print('A media de idade e {}'.format(media))