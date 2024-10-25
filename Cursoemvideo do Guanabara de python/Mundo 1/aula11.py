nome = 'Guanabara'
cor = {'limpa':'\033[m', 
        'azul':'\033[34m', 
        'amarelo':'\033[33m',
        'pretoebranco':'\033[7;37m'}
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(cor['pretoebranco'], nome, cor['limpa']))