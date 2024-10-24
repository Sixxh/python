#lista = [int(input('Digite um numero: ')), int(input('Digite um Numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: '))]
#maior = max(lista)
#menor = min(lista)
#print(f'O maior valor digitado foi {max(lista)} na posicao {lista.index(maior)+1}')
#print(f'O menor valor digitado foi {min(lista)} na posicao {lista.index(menor)+1}')
valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posicao {cont}: ')))
maior = max(valores)
menor = min(valores)
contmaior = 0
contmenor = 0
posmaior = []
posmenor = []
for c in valores:
    print(c)
    if maior == c:
        posmaior.append(valores.index(maior, contmaior))
        contmaior += 1
    if menor == c:
        posmenor.append(valores.index(menor, contmenor))
        contmenor += 1
print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for a in posmaior:
    print(a, end='... ')
print(f'\nO menor valor digitado foi {menor} nas posicoes ', end='')
for b in posmenor:
    print(b, end='... ')