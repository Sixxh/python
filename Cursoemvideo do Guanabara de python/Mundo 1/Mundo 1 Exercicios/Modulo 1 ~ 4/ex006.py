# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e a raiz quadrada.
# exemplo raiz quadrada 81 = 9 = 81**(1/2)
numero = int(input('Digite um numero: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
# print('O dobro de {} e {}'.format(numero, dobro))
# print('O triplo de {} e {}'.format(numero, triplo))
# print('A raiz quadrada de {} e {}'.format(numero, raiz))
# print('O dobro de {} e {}, o triplo e {} e a raiz quadrada e {}.'.format(numero, dobro, triplo, raiz))
# professor
print('O dobro de {} e {}.'.format(numero, (numero*2)))
print('O triplo de {} e {}. \nA raiz quadrada de {} e {:.2f}.'.format(numero, (numero*3), numero, pow(numero, (1/2))))
