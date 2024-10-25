# faca um programa que tenha uma funcao chamada area(), que receba as dimensoes de um terreno retangular(largura e copmirmento) e mostre a area do terreno.
def area(a, b):
    areatotal = a * b
    print(f'A area de um terreno {a}x{b} e de {areatotal}m')

print('Controle de Terrenos.')
print('-' * 23)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)