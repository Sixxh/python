# crie um programa que leia uma frase qualquer e diga se ela e um  palindromo, desconsiderando os espacos.
# ex: palindromo e uma frase que se vc ler de tras pra frente o resultado e o mesmo
# apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona
frase = str(input('Digite uma frase: ')).strip().upper()
tras = frase[::-1]
replace_frase = frase.replace(' ', '')
replace_tras = tras.replace(' ', '')
if replace_frase == replace_tras:
    print('Palindromo')
else:
    print('Nao e palindromo')
print(replace_frase, replace_tras)
