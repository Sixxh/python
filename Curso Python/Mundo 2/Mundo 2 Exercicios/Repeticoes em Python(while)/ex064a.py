# crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai para quando o usuario digitar o valor 999, que e a condicao de parada.
# no final, mostre quantos numeros foram digitador e qual foi a soma entre eles(desconsiderando o flag(999)).
num = cont = soma = 0
num = int(input('Digite um numero: [999 PARA PARAR] '))
while num != 999:    
    soma += num
    cont += 1
    num = int(input('Digite um numero: [999 PARA PARAR] '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))