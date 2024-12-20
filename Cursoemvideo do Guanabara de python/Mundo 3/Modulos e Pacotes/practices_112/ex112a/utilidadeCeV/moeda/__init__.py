def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato == False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/100)
    return res if not formato else moeda(res)

def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if not formato else moeda(res)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preco analizado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de reducao: \t{diminuir(preco, taxar, True)}')
    print('-' * 35)