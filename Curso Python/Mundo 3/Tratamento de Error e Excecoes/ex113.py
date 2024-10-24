def leiaInt(msg):
    try:
        ok = False
        valor = 0
        while True:
            n = str(input(msg))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('\033[0;31mERRO: Digite um numero inteiro valido.\033[m')
            if ok:
                break
        return valor
    except KeyboardInterrupt:
        print('O usuario preferiu nao digitar este numero')
        return 0

def leiafloat(msg):
    try:
        valido = False
        while not valido:
            entrada = str(input(msg)).replace(',', '.').strip()
            if entrada.isalpha() or entrada == '':
                print(f'\033[0;31mERRO: "{entrada}" e um preco invalido!\033[m')
            else:
                valido = True
                return float(entrada)
    except KeyboardInterrupt:
        print('O usuario preferiu nao digitar este numero')
        return 0

# Programa Principal
inteiro = leiaInt('Digite um numero Inteiro: ')
real = leiafloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')