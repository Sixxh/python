# ---------------------------------------------------------
# Comando para saber pra que serve uma funcao

# help() # abre cmg onde vc pode digitar qualquer comando que vai ter explicado oq ele faz
# help(print) # mostra oq o comando print faz
# print(print.__doc__) msm coisa q o help(print)

# ---------------------------------------------------------
# O que e uma docstring

# utiliza-se """ """ para escrever uma docstring(informacao sobre para que funciona a variavel) que pode ser lida usando o comando help()

# def contador(i, f, p):
#    """
#    -> Faz uma contagem e mostra na tela.
#    :paramentro i: inicio da contagem
#    :paramentro f: fim da contagem
#    :paramentro p: passo da contagem
#    :return: sem retorno
#    """
#    c = i
#    while c <= f:
#        print(f'{c} ', end='')
#        c += p
#    print('Fim!')
# help(contador)

# ---------------------------------------------------------
# Parametro opcional

# def somar(a=0,b=0,c=0): # quando vc atribui um valor ao parametro ele se torna um parametro opcional onde quando o usuario nao atribuir valor a ele, ele vai receber o valor que vc atribuiu como padrao.
#    """
#    Faz a soma de tres valores e mostra o resultado na tela
#    :param a: o primeiro valor
#    :param b: o segundo valor
#    :param c: o terceiro valor
#    """
#    s = a + b + c
#     print(f'A soma entre os valores e {s}')

# somar(3, 2, 5)
# somar(8, 4)
# somar()

# ---------------------------------------------------------
# escopo de variaveis ou escopo de declaracoes

# basicamente na programacao escopo eh o local onde uma variavel vai existir e um local onde uma variavel nao vai mais existir

# def teste():
#    n = 9
#    x = 8
#    print(f'na funcao teste, n vale {n}') # variaveis de escopo globais funcionam em escopo local sem problema, nesse caso a variavel {n} recebe o valor do escopo global isso caso n tenha uma variavel de mesmo nome dentro do escopo local como no exemplo abaixo.
#    print(f'Na funcao teste, n vale {n}') # caso exista uma variavel com o mesmo nome da variavel do escopo global o print vai priorizar a variavel do escopo onde ele esta nesse caso a variavel {n} vai receber o valor 9 ao inves de 2
#    print(f'Na funcao teste, x vale {x}')

# Programa Principal
# n = 2
# print(f'No programa principal n vale {n}')
# print(f'No programa principal x vale {x}') # nao funciona pq a variavel {x} esta em um escopo local entao so funciona no local onde foi criada
# teste(n)

# ---------------------------------------------------------
# Retorno de valores
# def somar(a=0, b=0, c=0):
#     s = a+b+c
#     return s # faz retorna a variavel {s} para o que estiver escrito antes da variavel no programa principal

# return pode tambem ser usado para retornar true or false

# Programa principal
# \/ return atribui a variavel {s} a {resp}
# resp = somar(2,3,5)
# print(resp)
# posso tambem utilizar o {print} e vai ter o mesmo resultado
# print(somar(4,7,8))
# fazendo uma funcao que retorna o resultado consigo fazer uma personalizacao dos resultados \/
# r1 = somar(2,7,9)
# r2 = somar(5,9)
# r3 = somar(6)
# print(f'O resultado das somas sao {r1}, {r2} e {r3}')

# ---------------------------------------------------------
# def factorial(num = 1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
# 
# n = int(input('Digite um Numero: '))
# print(f'O factorial de {n} e igual a {factorial(n)}')
# f1 = factorial(5)
# f2 = factorial(4)
# f3 = factorial()
# print(f'Os resultados sao {f1}, {f2} e {f3}')

def par(num = 0):
    if n % 2 == 0:
        return True
    else:
        return False

n = int(input('Digite um Numero: '))
if par(n):
    print('E par!')
else:
    print('Nao e par')