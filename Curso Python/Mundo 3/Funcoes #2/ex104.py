#crie um programa que tenha a funcao leiaint(), que vai funcionar de forma semelhante a funcao input() do python, so que fazendo a validacao para aceitar apenas um valor numerico. ex: n = leitaint('digite um n)
def leiaInt(num):
    while True:
        n = input(num)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('ERRO: Digite um numero inteiro valido.')
    return n
    
# Programa Principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')