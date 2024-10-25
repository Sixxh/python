lista = []
lista.append(str(input('Digite uma expressao: ')))
print(lista)
while True:
    if '(' in lista:
        if ')' in lista:
            print('A expressao esta fechada')
            break
        else:
            print('A expressao nao esta fechada')
            break