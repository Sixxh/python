# faca um programa que leia o ano de nascimento de um jovem e informa de acordo com sua idade:
# faca o programa pegar a data do computador
# se ele ainda vai se alistar ao servico militar
# se e a hora de se alistar
# se ja passou do tempo de alistamento
# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo
from datetime import date
nascimento = int(input('Qual ano voce nasceu? '))
ano = date.today().year - nascimento
if ano < 18:
    print('Faltam {} anos para voce se alistar'.format(18 - ano))
elif ano == 18:
    print('Voce ja tem a idade para se alistar')
elif ano > 18:
    print('Voce era para ter se alistado a {} anos'.format(ano - 18))