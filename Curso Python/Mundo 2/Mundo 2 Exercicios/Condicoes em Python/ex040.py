# crie um programa que leia dua snotas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo com a media atingida:
# media abaixo de 5.0: reprovado
# media entre 5.0 e 6.9: recuperacao
# media 7.0 ou superior: aprovado
nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual sua segunda nota? '))
cor = {'limpa':'\033[m', 'red':'\033[0;31m', 'yellow':'\033[0;33m', 'green':'\033[0;32m'}
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua media eh {}{:.1f}{} e voce foi reprovado.'.format(cor['red'], media, cor['limpa']))
elif 6.9 >= media >= 5.0:
    print('Sua media eh {}{:.1f}{} e voce esta de recuperacao.'.format(cor['yellow'], media, cor['limpa']))
elif media >= 7.0:
    print('Sua media eh {}{:.1f}{} e voce esta aprovado.'.format(cor['green'], media, cor['limpa']))
