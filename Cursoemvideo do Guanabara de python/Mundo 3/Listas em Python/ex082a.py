lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar? ')).strip().upper()[0]
    if continuar in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)
print(f'A lista completa e {lista}')
print(f'A lista de pares e {par}')
print(f'A lista de impares e {impar}')