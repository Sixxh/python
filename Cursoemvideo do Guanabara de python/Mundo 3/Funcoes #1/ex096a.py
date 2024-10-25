def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno com {larg}x{comp} e de {a}m2.')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)