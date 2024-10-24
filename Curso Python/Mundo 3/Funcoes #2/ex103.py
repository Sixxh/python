# faca um programa que tenha uma funcao chamada ficha(), que receba doi parametros opcionais: o nome de um jogador e quantos gold ele marcou.
# O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado corretamente.
def ficha(name = '<Desconhecido>', goals = 0):
    print(f'O jogador {name} fez {goals} gol(s) no campeonato.')

# Programa Principal
nome = str(input('Nome do Jogador: '))
if nome in '':
    nome = '<Desconhecido>'
gols = input('Numero de Gols: ')
if gols == '':
    gols = 0
ficha(nome,gols)