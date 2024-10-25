# faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# ex: digite um numero: 1834
# unidades: 4
# dezenas: 3
# centena: 8
# milhar: 1

#meu

#num = str(input('Digite um numero de 0 a 9999: '))
#print('A Unidade e:', num[3])
#print('A Dezena e:', num[2])
#print('A Centena e:', num[1])
#print('O Milhar e:', num[0])

#professor

num = int(input('Informe numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))