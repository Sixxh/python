# crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome
nome = str(input('Digite seu nome: ')).strip()
print('Voce tem silva no nome? {}'.format('silva' in nome.lower()))