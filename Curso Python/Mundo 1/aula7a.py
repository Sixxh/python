# nome = input('Qual o seu nome? ')
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'.format(nome))
# print('Prazer em te conhecer {:^20}!'.format(nome))
# print('Prazer em te conhecer {:-^20}!'.format(nome))
n1 = int(input('Um Valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('A soma vale {}, \no produto vale {} \ne a divisao vale {:.3f}.'.format(s, m, d), end=' ')
print('A divisao inteira e {} e a potencia {}.'.format(di, e))
print('O resto da divisao e {}'.format(r))