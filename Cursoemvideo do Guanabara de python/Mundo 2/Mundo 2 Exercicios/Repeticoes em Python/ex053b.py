# crie um programa que leia uma frase qualquer e diga se ela e um  palindromo, desconsiderando os espacos.
# ex: palindromo e uma frase que se vc ler de tras pra frente o resultado e o mesmo
# apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Palindromo')
else:
    print('Nao e palindromo')