import random
maior = menor = 0
cont = 0
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
lista = list(tup)
random.shuffle(lista)
lista2 = lista[:5]
print(lista[:5])
print(min(lista2))
print(max(lista2))