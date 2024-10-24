def moeda(p):
    edit = f'R$ {p:.2f}'
    return edit

def metade(p, form=False):
    res = p / 2
    if form:
        return moeda(res)
    else:
        return res

def dobro(p, form=False):
    res = p * 2
    if form:
        return moeda(res)
    else:
        return res

def aumentar(p, taxa, form=False):
    porc = taxa / 100
    res = p + (p * porc)
    if form:
        return moeda(res)
    else:
        return res

def diminuir(p, taxa, form=False):
    porc = taxa / 100
    res = p - (p*porc)
    if form:
        return moeda(res)
    else:
        return res
    
def resumo(p, aum=0, redu=0):
    res = 'RESUMO DO VALOR'
    linhas = len(res) + 14
    espaco = 7
    print('-' * linhas)
    print(f'{' '* espaco}{res}{' '* espaco}')
    print('-' * linhas)
    print(f'Preco analisado: {moeda(p)}')
    print(f'Dobro do preco: {dobro(p, True)}')
    print(f'Metade do Preco: {metade(p, True)}')
    print(f'{aum}% de aumento: {aumentar(p, aum, True)}')
    print(f'{redu}% de reducao: {diminuir(p, redu, True)}')
    print('-' * linhas)