arq = 'ex12.txt'

with open(arq, 'w+') as e:
    e.write('asdf')

a = open(arq, 'r')

for linha in a:
    print(linha)
