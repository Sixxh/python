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