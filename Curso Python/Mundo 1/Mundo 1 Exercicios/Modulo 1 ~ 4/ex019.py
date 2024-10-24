#um professor quer sortear um dos seus quatro alunos para apagar o quadro, faca um programa que ajude ele, lendo o nome deles
#e escrevendo o nome do escolhido
from random import choice
a = str(input('Digite o nome do aluno a: '))
b = str(input('Digite o nome do aluno b: '))
c = str(input('Digite o nome do aluno c: '))
alunos = [a, b, c]
random = choice(alunos)
print('O aluno escolhido e: {}'.format(random))