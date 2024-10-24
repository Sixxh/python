def metade(p):
    return p / 2

def dobro(p):
    return p * 2

def aumentar(p, taxa):
    porc = taxa / 100
    return p + (p * porc)

def diminuir(p, taxa):
    porc = taxa / 100
    return p - (p * porc)

def moeda(p):
    edit = f'R$ {p:.2f}'
    return edit