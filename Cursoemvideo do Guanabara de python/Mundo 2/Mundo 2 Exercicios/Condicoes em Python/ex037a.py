# escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao
# 1 para binario
# 2 para octal
# 3 para hexaadecimal
n = int(input('Qual Numero deseja converter? '))
print('''Digite 
      [ 1 ] para Binario 
      [ 2 ] para Octal
      [ 3 ] para Hexaadecimal''')
base = int(input('Qual base de conversao ? '))
if base == 1:
    print('O numero {} convertido para Binario e {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('O numero {} convertido para Octal e {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('O numero {} convertido para Hexaadecimal e {}'.format(n, hex(n)[2:]))
else:
    print('Escolha entre as opcoes 1 e 3')
