time = ('atletico-pr', 'bahia', 'flamengo', 'botafogo', 'sao paulo', 'cruzeiro', 'atletico-mg', 'bragantino', 'palmeiras', 'internacional', 'fortaleza', 'gremio', 'vasco da gama', 'criciuma', 'juventude', 'corinthians', 'fluminense', 'ec vitoria', 'atletico-go', 'cuiaba')
print('=' * 30)
print(f'A lista dos teims do brasileirado: {time}')
print('=' * 30)
print(f'Os 5 primeiros colocados sao: {time[0:5]}')
print('=' * 30)
#print(f'Os 4 ultimos sao: {time[-1:-5:-1]}')
print(f'Os 4 ultimos sao: {time[-4:]}')
print('=' * 30)
print(f'Times em ordem alfabetica: {sorted(time)}')
print('=' * 30)
print(f'O gremio esta na {time.index('gremio')+1} posicao.')
print('=' * 30)