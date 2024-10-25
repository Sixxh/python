# faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor
n1 = float(input('Digite um Numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite outro numero: '))
lista = [n1, n2, n3]
print('O menor numero e {:.2f}'.format(min(lista)))
print('O maior numero e {:.2f}'.format(max(lista)))