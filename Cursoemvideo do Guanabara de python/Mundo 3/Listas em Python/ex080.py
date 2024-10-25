# crie um progbrama onde o usuario possa digitar cinco valores numericos e cadastreos em uma lista, ja na posicao correta de insercao(sem usar o sort). no final mostre a lista ordedana.
lista = []
mai = 0
men = 0
cont = 0
for c in range(0, 5):
    num = int(input('Digite um numero: '))
    if c == 0:
        mai = men = num
        lista.append(num)
    else:
        if num > mai:
            mai = num
            lista.append(num)
            print('O numero foi adicionado no final da lista')
        if num < men:
            men = num
            lista.insert(0, num)
            print('O numero foi adicionado no comeco da lista')
print(lista)