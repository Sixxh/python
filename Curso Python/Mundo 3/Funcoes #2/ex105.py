# faca um programa que tenha uma funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes.
# quantidade de notas
# a maior nota
# a menor nota
# a media da turma
# a situacao(opcional)
# adicione tambem as docstrings da funcao
def notas(* num, sit=False):
    """-> Funcao para analisar notas e situacoes de varios alunos. 
    :param num: uma ou mais notas dos alunos(aceita varias notas).
    :param sit: valor opcional, indicando se deve ou nao adicionar a situacao."""
    geral = dict()
    maior = menor = tot = 0
    for cont, valor in enumerate(num):
        print(cont, valor)
        tot += valor
        if cont == 0:
            maior = valor
            menor = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
    med = tot / len(num)
    geral['total'] = len(num)
    geral['maior'] = maior
    geral['menor'] = menor
    geral['media'] = med
    if sit:
        situ = ''
        if med >= 7:
            situ = 'BOA'
        elif 7 > med >= 5:
            situ = 'RAZOAVEL'
        elif med < 5:
            situ = 'RUIM'
        geral['situacao'] = situ
    print(geral)

# programa principal
resp = notas(9, 7, 6.5, 7, 4, sit=True)
print(resp)