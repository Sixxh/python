# o mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos
# faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a = str(input('Digite nome do aluno a: '))
b = str(input('Digite nome do aluno b: '))
c = str(input('Digite nome do aluno c: '))
d = str(input('Digite nome do aluno d: '))
alunos = [a, b, c, d]
shuffle(alunos)
print('A ordem de apresentacao e: {}'.format(alunos))