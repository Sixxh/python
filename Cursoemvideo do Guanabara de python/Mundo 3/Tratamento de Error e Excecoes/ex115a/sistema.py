from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opcao de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opcao de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opcao de sair do sistema
        cabecalho('Saindo do sistema... Ate logo!')
        break
    else:
        # Digitou uma opcao errada no menu
        print('\033[31mERRO: Digite uma opcao valida!\033[m')
    sleep(1)