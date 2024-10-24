dados = dict()
lista = list()
listaf = list()
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas')
for c in range(len(lista)):
    if lista[c]['sexo'] == 'F':
        listaf.append(lista[c]['nome'])
print(listaf)