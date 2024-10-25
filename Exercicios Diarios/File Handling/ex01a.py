arq = 'ex12a.txt'

# write to the file
with open(arq, 'w+') as e:
    e.write('asdf')

# read from the file
with open(arq, 'r') as a:
    for linha in a:
        print(linha)