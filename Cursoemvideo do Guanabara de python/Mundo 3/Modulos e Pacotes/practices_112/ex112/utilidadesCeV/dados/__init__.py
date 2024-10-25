def leiadinheiro(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'ERRO! "{input(msg)}" e um preco invalido!')
        if ok:
            break
    return valor