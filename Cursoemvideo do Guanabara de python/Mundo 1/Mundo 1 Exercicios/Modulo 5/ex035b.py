# professor
print('-=-' * 20)
print('Analisando Possibilidade de Triangulo')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento acima podem formar um triangulo')
else:
    print('Os segmentos acima nao podem formar um triangulo')