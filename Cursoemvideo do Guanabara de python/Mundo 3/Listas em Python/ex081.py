lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
lista.sort(reverse=True)
print(f'Voce digitou {len(lista)} elementos')
print(f'O valor em ordem descrescente sao {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 nao faz parte da lista')