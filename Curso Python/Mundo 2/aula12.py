nome = str(input('Qual o seu nome: '))
if nome == 'Gabriel':
    print('Pro')
elif nome == 'Pedro' or nome == 'Joao' or nome == 'Julia':
    print('Nome normal')
elif nome in 'Ana Claudia Joana Juliana':
    print('Nome feminino normal')
else:
    print('Nah, newbie total')
print('Tenha um bom dia, {}!'.format(nome))