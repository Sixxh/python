# escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao
# 1 para binario
# 2 para octal
# 3 para hexaadecimal
n = int(input('Qual Numero deseja converter? '))
print('Digite 1 para Binario 2 Para Octal e 3 para Hexaadecimal')
base = int(input('Qual base de conversao ? '))
if base == 1:
    binario = bin(n)
    print('O numero desejado convertido para Binario e {}{}{}'.format('\033[0;31m', binario[2::], '\033[m'))
elif base == 2:
    octal = oct(n)
    print('O numero desejado convertido para Octal e {}{}{}'.format('\033[0;31m', octal[2::], '\033[m'))
elif base == 3:
    hexa = hex(n)
    print('O numero desejado convertido para Hexaadecimal e {}{}{}'.format('\033[0;31m', hexa[2::], '\033[m'))
else:
    print('Escolha entre as opcoes 1 e 3')
