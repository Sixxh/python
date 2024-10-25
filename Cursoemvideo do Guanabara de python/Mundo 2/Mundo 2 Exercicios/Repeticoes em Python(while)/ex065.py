# crie um programa que leia varios numeros inteiros pelo teclado. no final da execucao, 
# mostre a media entre todos os valores e qual foi o maior e menor valores lidos.
# o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valroes.
quantidade = 0
soma = 0
maior = 0
menor = 0
continuar = 0
while continuar != 1:
    for c in range(1, 5):
        n = int(input('Digite um numero: '))
        quantidade += 1
        soma += n
        if menor == 0 and maior == 0:
            maior = n
            menor = n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = int(input('''Deseja digitar mais numeros ou finalizar? 
[0]Continuar
[1]Finalizar
Qual sua escolha? '''))
media = soma / quantidade
print('O maior numero foi {}.'.format(maior))
print('O menor numero foi {}.'.format(menor))
print('A media entre os numeros digitados foi {}.'.format(media))