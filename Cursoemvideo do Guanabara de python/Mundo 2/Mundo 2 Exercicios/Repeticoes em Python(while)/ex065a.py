# crie um programa que leia varios numeros inteiros pelo teclado. no final da execucao, 
# mostre a media entre todos os valores e qual foi o maior e menor valores lidos.
# o programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valroes.
resp = 'S'
soma = quantidade = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
media = soma / quantidade
print('Voce digitou {} e a media entre eles e {:.2f}'.format(quantidade, media))
print('O maior valor foi {} e o menor foi {} '.format(maior, menor))