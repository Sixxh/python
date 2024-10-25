# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
# A media de idade do grupo.
# qual e o nome do homem mais velho.
# quantas mulheres tem menos de 20 anos.
somaidade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0
for p in range(1, 5):
    print('----- {} PESSOAA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        tot_mulher_20 += 1

media_idade = somaidade / 4
print('A media de idade do grupo e de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Apenas {} mulheres tem menos de 20 anos.'.format(tot_mulher_20))