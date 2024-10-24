# melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# o programa encerra quando ele disser que quer mostrar 0 termos.
repeticao = 0
termo = int(input('Termo: '))
razao = int(input('Razao: '))
prog = termo
while repeticao != 10:
    prog += razao
    repeticao += 1
    print(prog, end=' -> ')
    if repeticao == 10:
        repeticao = int(input('\nDeseja continuar? \n0-sim 10-nao: '))