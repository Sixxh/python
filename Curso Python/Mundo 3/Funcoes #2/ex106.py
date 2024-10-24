# faca um mini-sistema que utilize o interactive help do python. O usuario vai digitar o comando e o manual vai aparecer. Quando o usuario digitar a palavra 'FIM', o programa se encerrara. OBS: Use cores

def edicao(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

def bibli(msg):
    from time import sleep
    edicao(f'Acessando o manual do comando {msg}')
    sleep(0.5)
    help(f'{msg}')


# Programa Principal
while True:
    edicao('SISTEMA DE AJUDA PyHELP')
    perg = str(input('Funcao ou Biblioteca: ')).strip().lower()
    if perg in 'fim':
        edicao('Finalizando programa')
        break
    bibli(perg)