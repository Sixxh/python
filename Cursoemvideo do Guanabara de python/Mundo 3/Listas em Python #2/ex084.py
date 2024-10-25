# faca um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. no final mostre
# a) quantas pessoas foram cadastradas.
# b) uma listagem com as pessoas mais pesadas
# c) uma listagem com as pessoas mais leves
geral = list()
pcad = list()
maiorp = menorp = 0
while True:
    geral.append(str(input('Nome: ')))
    geral.append(float(input('Peso: ')))
    pcad.append(geral[:])
    continuar = str(input('Deseja continuar? ')).upper().strip()[0]
    if continuar in 'N':
        break
    geral.clear()
maiorn = ''
menorn = ''
for p, v in enumerate(pcad):
    if menorp == 0:
        menorp = v[1]
    if v[1] > maiorp:
        maiorp = v[1]
        maiorn = v[0]
    if v[1] < menorp:
        menorp = v[1]
        menorn = v[0]
print('-=' * 30)
print(f'O maior peso cadastrado foi de {maiorp}. Peso de {maiorn}')
print(f'O menor peso cadastrado foi de {menorp}. Peso de {menorn}')
print(f'Ao todo, voce cadastrou {len(pcad)} pessoas.')