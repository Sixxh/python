# def soma(a, b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma {a} + {b} = {s}')

#soma(4, 5)
#soma(a=7, b=8)

# ----------------------------------

# def contador(* num):
#    tam = len(num)
#    print(f'Recebi os valores {num} e sao ao todo {tam} numeros')
#    for valor in num:
#        print(f'{valor} ', end='')
#    print('Fim')

#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

# ----------------------------------
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)