# crie um programa qe tenha uma tupla com varias palavras(nao usar acento). depois disso, voce deve mostrar, para cada palavra, quais sao as suas vogais
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador')
var = 0
varpalavras = 0
test = palavras[0]
voga = ('a', 'e', 'i', 'o', 'u')
print(f'A palavra {palavras[var]} tem ', end='')
while True:
    contar = test.count(voga[var])
    if contar != 0:
        print(voga[var], end=' ')
    var += 1
    if contar == 0:
        break