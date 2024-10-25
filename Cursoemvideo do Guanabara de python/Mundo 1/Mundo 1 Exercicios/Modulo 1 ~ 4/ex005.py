# Faca um programa que leia um numero Inteiro e mostre na tela o seu sucessor e seu antecessor.
# exemplo o sucessor do numero 5 e 6 e o antecessor e 4
numero = int(input('Digite um numero: '))
sucessor = numero + 1
antecessor = numero - 1
# print('O sucessor de {} e {} e o antecessor e {}'.format(numero, sucessor, antecessor))
# professor
print('O sucessor de {} e {} e o atecessor e {}'.format(numero,(numero+1),(numero-1)))