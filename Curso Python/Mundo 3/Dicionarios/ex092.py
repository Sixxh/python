# se aposenta com 35 anos contribuido
import datetime
data_atual = datetime.datetime.now()
ano = data_atual.year
dados = dict()
dados['nome'] = str(input('Nome: '))
ida = ano - int(input('Ano de nascimento: '))
dados['idade'] = ida
carteira = int(input('Carteida de Trabalho (0 nao  tem): '))
dados['ctps'] = carteira
if carteira != 0:
    anocont = int(input('Ano de contratacao: '))
    dados['contratacao'] = anocont
    dados['salario'] = float(input('Salario: '))
    aposen = 35 - (ano - anocont) + ida
    dados['aposentadoria'] = aposen
print('-=' * 30)
for v, c in dados.items():
    print(f'{v} tem o valor {c}')