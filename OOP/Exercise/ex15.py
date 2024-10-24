def CriarArq(arq):
    try:
        with open(arq, 'x') as file:
            file.close()
    except FileExistsError:
        return 'Arquivo ja Existe'
    except Exception as e:
        return f'ERROR: {e}'
    else:
        return 'Arquivo criado com sucesso'

def LerInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print ('Digite um valor numerico inteiro valido.')
        except Exception as e:
            print(f'ERROR ao transformar em numero inteiro: {e}')
        else:
            return n
        
def cabecalho(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)

def linha(num):
    print('-' * num)

def EscreverArq(arq, task):
    try:
        with open(arq, 'a') as file:
            file.write(f'{task} | Incompleto\n')
    except Exception as e:
        print(f'ERRO ao escrever no arquivo: {e}')

def LerArq(arq):
    try:
        with open(arq, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print('Arquivo nao encontrado')
    except Exception as e:
        print(f'ERRO ao ler o arquivo: {e}')

def Mudar(arq, nome):
    try:
        with open(arq, 'r') as file:
            tasks = file.readlines()
        with open(arq, 'w') as file:
            for task in tasks:
                task_data = task.split(' | ')
                if task_data[0] == nome:
                    file.write(f'{task_data[0]} | Completed\n')
                else:
                    file.write(task)
    except Exception as e:
        print(f'ERRO atualiznado tarefas: {e}')

def menu1():
    cabecalho('Adicionando Tarefa!')
    tarefa = str(input('Nome da Tarefa? '))
#     while True:
#             cabecalho('Status da tarefa')
#             print("""• 1 - Incompleta
# • 2 - Completa""")
#             linha(30)
#             opc = LerInt('Status: ')
#             if opc == 1:
#                 status = 'Incompleta'
#                 break
#             elif opc == 2:
#                 status = 'Completa'
#                 break
#             else:
#                 print('Digite uma das opcoes validas: ')
    EscreverArq(arq, tarefa)
    return tarefa

def Deletar(arq, nome):
    try:
        with open(arq, 'r') as file:
            tasks = file.readlines()
            print(tasks)
        with open(arq, 'w') as file:
            for task in tasks:
                task_data = task.split(' | ')
                print(task)
                if task_data[0] != nome:
                    file.write(task)
    except Exception as e:
        print(f'ERRO ao deletar tarefa: {e}')

# Programa Principal
arq = 'tasklist.txt'
if CriarArq(arq) == 'Arquivo criado com sucesso':
    print(f'Arquivo {arq} foi criado')

num = 0
while True:
    cabecalho('TO-DO List')
    print("""• 1 - Adicionar Tarefa
• 2 - Listar Tarefas
• 3 - Mudar Status da tarefa
• 4 - Deletar Tarefa
• 5 - Parar Programa""")
    linha(30)
    num = LerInt('O que deseja? ')
    if num == 1:
        menu1()
    elif num == 2:
        LerArq(arq)
    elif num == 3:
        task_nome = str(input('Qual nome da tarefa que foi completada? '))
        Mudar(arq, task_nome)
    elif num == 4:
        task_nome = str(input('Qual nome da tarefa que deseja deletar? '))
        Deletar(arq, task_nome)
    elif num == 5:
        print('Fechando...')
        break
    else:
        print('Digite uma opcao valida.')