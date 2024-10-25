# crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a media de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.
listona = list()
listanome = list()
listanota = list()
listann = list()
while True:
    listanome.append(str(input('Nome: ')))
    listann.append(listanome[:])
    listanota.append(float(input('Nota 1: ')))
    listanota.append(float(input('Nota 2: ')))
    listann.append(listanota[:])
    listona.append(listann[:])
    listann.clear()
    listanome.clear()
    listanota.clear()
    continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print(listona)
for v, b in enumerate(listona):
    if v == 0:
        soma = listona[v][1]
        print(f'{v} {listona[v][v]}')

    