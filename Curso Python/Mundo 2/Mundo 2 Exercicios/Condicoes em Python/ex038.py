# escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# o primeiro valor e maior
# o segundo valor e maior
# nao existe valor maior, os dois sao iguais
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
    print('O primeiro valor e maior.')
elif a < b:
    print('O segundo valor e maior.')
elif a == b:
    print('Nao existe valor maior os dois sao iguais')