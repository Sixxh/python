def criararq(arq):
    try:
        with open(arq, 'x') as file:
            file.close
    except FileExistsError:
        return 'Arquivo ja existe'
    else:
        return 'Arquivo Criado'

def EscreverArq(arq, msg):
    with open(arq, 'a') as file:
        file.write(f'Name: {msg}\n')

def LerArq(arq):
    with open(arq, 'r') as file:
        for line in file:
            print(line.strip())


arq = 'exercise2.txt'

criararq(arq)

while True:
    name = str(input('Digite seu Nome: [STOP PARA ENCERRAR]'))
    if name.strip().upper() == 'STOP':
        break
    EscreverArq(arq, name)

LerArq(arq)