# refaca o desafio 009, mostrando a tabuada de um numero q o usuario escolher so que agora utilizando FOR
# n = int(input('Digite o numero que deseja ver a tabuada: '))
# for c in range(1, 11):
#     r = n * c
#     print('{} x {} = {}'.format(n, c, r))

# professor

n = int(input('Digite um numero que deseja ver a tabuada: '))
for c in range (1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))