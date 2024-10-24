from datetime import datetime
def voto(num):
    tipo = ''
    idade = datetime.now().year - anonasc
    if idade < 16:
        tipo = 'NAO VOTA'
    if idade >= 16 and idade < 18 or idade > 65:
        tipo = 'VOTO OPCIONAL'
    if idade >= 18 and idade <= 65:
        tipo = 'VOTO OBRIGATORIO'
    print(f'Com {idade} anos: ', end='')
    return tipo

anonasc = int(input('Qual seu ano de nascimento? '))

print(f'VOTO {voto(anonasc)}.')