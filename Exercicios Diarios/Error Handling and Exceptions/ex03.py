def CriarArquivo(arq):
    try:
        with open(arq, 'x') as file:
            file.close()
    except FileExistsError:
        print('Arquivo ja existe!')
    except Exception as e:
        print(f'Erro: {e}')
    else:
        print('Arquivo Criado!')

def EscreverArq(arq, nome, score):
    with open(arq, 'a') as file:
        file.write(f'{nome}: {score}\n')

def LerArq(arq):
    with open(arq, 'r') as file:
        for line in file:
            print(line.strip())

def LerInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um valor inteiro valido')
        except KeyboardInterrupt:
            print('Usuario preferiu nao digitar')
            return 0
        else:
            return num

arq = 'name_score.txt'

CriarArquivo(arq)

while True:
    nome = str(input('Nome: '))
    score = LerInt('Score: ')
    EscreverArq(arq, nome, score)
    continuar = str(input('Deseja Continuar? [S/N]'))
    while continuar.strip().upper()[0] not in 'SN':
            continuar = str(input('Por favor digite S ou N: '))
    if continuar.strip().upper()[0] == 'N':
        break
    elif continuar.strip().upper()[0] == 'S':
        continue

LerArq(arq)