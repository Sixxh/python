# faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'm' ou 'f'.
# caso esteja errado peca a digitacao novamente ate ter um valor correto.
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual seu sexo [M/F] ? ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Digite novamente!')
print('Seu sexo e {}'.format(sexo))