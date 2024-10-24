# crie um programa que leia o nome completo de uma pessoa e mostre
# o nome com todas as letras maiusculas
# o nome com todas minusculas
# quantas letras ao todo (sem considerar espacos)
# quantas letras tem o primeiro nome

#meu

#nome = str(input('Qual o seu nome: '))
#separar =  nome.split()
#unir = ''.join(separar)
#print('Maiusculo:', nome.upper())
#print('Minusculo:', nome.lower())
#print('O nome tem ao todo tem:', len(unir))
#print('O primeiro nome tem:', len(separar[0]))

#professor

nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maisculas e: {}'.format(nome.upper()))
print('Seu nome em minusuclas e: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome e {} e ele tem {} letras'.format(separa[0], len(separa[0])))

