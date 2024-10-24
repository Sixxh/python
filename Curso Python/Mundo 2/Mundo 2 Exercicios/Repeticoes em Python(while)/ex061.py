# refaca o desafio 051, lendo o primeiro termo e a razao de uma pa, mostrando os 10 primeiros termos da progressao usando a estrutura while.
# desenvolva um programa que leia o primeiro termo e a razao de uma Progressao Aritimetica. No final, mostre os 10 primeiros termos desa progressao.
# termo = int(input('Termo: '))
# razao = int(input('Razao: '))
# max = termo + (10 - 1) * razao
# for c in range(termo, max + razao, razao):
#     print(c, end=' -> ')

repeticao = 0
termo = int(input('Termo: '))
razao = int(input('Razao: '))
prog = termo
while repeticao != 9:
    prog += razao
    repeticao += 1
    if repeticao == 1:
        print(termo, end=' -> ')
    print(prog, end=' -> ')
print('Fim', end='')