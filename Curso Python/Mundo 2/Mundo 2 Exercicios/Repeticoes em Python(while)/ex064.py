# crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai para quando o usuario digitar o valor 999, que e a condicao de parada.
# no final, mostre quantos numeros foram digitador e qual foi a soma entre eles(desconsiderando o flag(999)).
n = 0
soma = 0
digitado = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n != 999:
        soma += n
        digitado += 1
print(soma)
print(digitado)