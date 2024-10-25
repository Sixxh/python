#crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e a condicao de parada. no final, mostre quantos numeros foram digitador e qual foi a soma entre eles.(desconsiderando o flag).
soma = quant = 0
while True:
    n = int(input('Digite um numero: (Para parar digite 999) '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Voce digitou {quant} numeros e a soma entre eles e {soma}')