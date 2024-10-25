# refaca o desafio 051, lendo o primeiro termo e a razao de uma pa, mostrando os 10 primeiros termos da progressao usando a estrutura while.
# desenvolva um programa que leia o primeiro termo e a razao de uma Progressao Aritimetica. No final, mostre os 10 primeiros termos desa progressao.
print('Gerador de PA')
print('-=' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM', end='')