# faca um programa que leia o sexo de uma pessoa, mas so aceite os valores 'm' ou 'f'.
# caso esteja errado peca a digitacao novamente ate ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))