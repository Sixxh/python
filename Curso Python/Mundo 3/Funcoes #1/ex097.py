# faca um programa que tenha uma funcao chamada escreva(). que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel. ex: escreva('ola mundo')
# saida -----------
#        Ola Mundo
#       -----------
def escreva(txt):
    calc = len(txt)
    print('-' * calc)
    print(txt)
    print('-' * calc)

palavra = str(input('Qual palavra deseja ver? '))
escreva(f' {palavra} ')