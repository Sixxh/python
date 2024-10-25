# desenvolva um programa que leia o primeiro termo e a razao de uma Progressao Aritimetica. No final, mostre os 10 primeiros termos desa progressao.
termo = int(input('Termo: '))
razao = int(input('Razao: '))
max = termo + (10 - 1) * razao
for c in range(termo, max + razao, razao):
    print(c, end=' -> ')