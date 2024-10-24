# faca  um programa que calcule a soma entre todos os numeros impares que sao multiplo de tres e que se encontram no intervalo de 1 ate 500
#s = 0
#for c in range(1, 500):
#    if (c % 2) != 0:
#       s = s + c
#print(s)

#professor
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s = s + c
print(s)
print(cont)