s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
nome = 'Jose'
idade = 33
salario = 987
print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}')