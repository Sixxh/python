def lerInt(msg):
    ok = False
    while not ok:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO: por favor, digite um numero inteiro valido.')
    return valor

def lerEscolha(msg):
    ok = False
    while not ok:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO: Escolha uma opcao valida.')
    return valor

def cadastro(msg):
    edit('NOVO CADASTRO')
    nome = str(input('Nome: '))
    idade = lerInt('Idade: ')
    cadastros['nome'] = nome
    cadastros['idade'] = idade
    listacompleta.append(cadastros.copy())
    cadastros.clear()
    msg = print(f'Novo registro de {nome} adicionado.')
    save_file('listacompleta.txt')
    return msg

def edit(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)

def save_file(filename):
    with open(filename, 'w') as file:
        for item in listacompleta:
            file.write(f'{item['nome']}\t{item['idade']}\n')
    print(f'Lista salva em {filename}')

def load_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                nome, idade = line.strip().split('\t')
                listacompleta.append({'nome': nome, 'idade': int(idade)})
    except FileNotFoundError:
        print('Arquivo nao encontrado. Comecando com uma lista vazia.')

cadastros = dict()
listacompleta = list()
load_file('listacompleta.txt')

# Programa principal
while True:
    edit('MENU PRINCIPAL')
    print("""1 - Ver Pessoas Cadastradas
2 - Cadastrar nova Pessoa
3 - Sair do Sistema""")
    print('-' * 30)
    escolha = lerInt('Qual sua escolha? ')
    if escolha == 1:
        edit('PESSOAS CADASTRADAS')
        #for c, v in enumerate(listacompleta):
        #    print(f'{v['nome']}\t{v['idade']} anos')
        if listacompleta:
            for v in listacompleta:
                print(f"{v['nome']}\t{v['idade']} anos")
        else:
            print("Nenhuma pessoa cadastrada.")
    elif escolha == 2:
        cadastro('')
    elif escolha == 3:
        break
    else:
        print('ERRO: Escolha um opcao valida')
        continue