# refaca o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# equilateero: todos os lados iguais
# isosceles: dois lados iguais
# escaleno: todos os lados diferentes
print('-=-' * 20)
print('Analisando Possibilidade de Triangulo')
print('-=-' * 20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
pode = 0
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    pode = 1
    print('Os segmento acima podem formar um triangulo')
else:
    print('Os segmentos acima nao podem formar um triangulo')
if pode == 1 and r1 == r2 and r1 == r3:
    print('E o triangulo formado sera equilatero')
elif pode == 1 and r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
    print('E o triangulo formado sera isosceles')
elif pode == 1 and r1 != r2 and r1 != r3 and r2 != r1 and r2 != r3 and r3 != r1 and r3 != r2:
    print('E o triangulo formado sera Escaleno')