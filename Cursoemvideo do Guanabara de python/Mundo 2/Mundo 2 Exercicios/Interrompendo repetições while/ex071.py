# crie um programa que simule o funcionamento de um caixa eleetronico. no inicio, pergunte ao usuario qual ser ao valor a ser sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# obs: considere que o caixa possui cedulas de 50, 20, 10 e 1
valor = int(input('Qual valor deseja sacar? '))
resultado = 0
while True:
    if valor >= 50:
        soma = valor // 50
        resultado = valor - (soma * 50)
        print(f'Voce ira precisar de {soma}x cedulas de 50')
    if resultado >= 20:
        soma = resultado // 20
        resultado -= (soma * 20)
        print(f'Voce ira precisar de {soma}x cedulas de 20')
    if resultado >= 10:
        soma = resultado // 10
        resultado -= (soma * 10)
        print(f'Voce ira precisar de {soma}x cedulas de 10')
    if resultado >= 1:
        soma = resultado // 1
        resultado -= (soma * 1)
        print(f'Voce ira precisar de {soma}x cedulas de 1')
    if resultado == 0:
        break
print('FIM')