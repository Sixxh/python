from uteis import numeros
#Programa Principal
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} e {fat}')
print(f'O dobro de {num} e {numeros.dobro(num)}')
print(f'O triplo de {num} e {numeros.triplo(num)}')