import re

numeros = input('Qual seu numero? ')

# padroes = r'\b[0-9._%+-]+[0-9._%+-]+\b'
padroes = r'^(?:\+?\d{1,3}[-.\s]?)?(?:\(\d{2,4}\)|\d{2,4})[-.\s]?\d{3,5}[-.\s]?\d{3,5}$'

verificando = re.search(padroes, numeros)

if verificando:
    print(f'Se numero: {verificando.group()} eh valido')
else:
    print('numero invalido')