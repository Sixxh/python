lista = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    continuar = str(input('Deseja continuar? ')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'A lista com todos os valores digitados foi {lista}')
print(f'A lista com os valores pares {listapar}')
print(f'A lista com os valores impares {listaimpar}')