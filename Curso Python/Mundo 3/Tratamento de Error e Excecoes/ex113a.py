def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um numero inteiro valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n
    
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um numero real valido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mUsuario preferiu nao digitar esse numero.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um Inteiro: ')
n2 = leiaFloat('Digite um Real:')
print(f'O valor inteiro digitado foi {n1} e o real {n2}')