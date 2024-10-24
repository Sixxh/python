def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criacao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        for linha in a:
            print(f'{linha:<30}')
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()

arq = 'arquivo1.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

nome = str(input('Nome: '))
cadastrar(arq, nome)
lerArquivo(arq)