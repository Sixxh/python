# escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia de fibonacci.
# ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
n = int(input('Digite um numero: '))
resultado = 0
soma = 1
parar = 0
while parar != n:
    resultado += soma
    soma += resultado
    parar += 1
    print('{} + {}'.format(resultado, soma), end=' -> ')