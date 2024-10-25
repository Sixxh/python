dados = dict()
dados['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input('Quantas partidas ele jogou? '))
totgols = 0
for c in range(partidas):
    gols = int(input(f'Quantas gols ele fez na partida {c+1}? '))
    dados[f'partida {c+1}'] = gols
    totgols += gols
dados['gols'] = totgols
print(dados)