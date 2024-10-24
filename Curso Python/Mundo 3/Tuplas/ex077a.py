# crie um programa qe tenha uma tupla com varias palavras(nao usar acento). depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')