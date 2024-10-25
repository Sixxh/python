import re

email = str(input('Qual seu email? '))

padrao = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.]+\.[A-Za-z]{2,7}$'

tenta = re.search(padrao, email)
if tenta:
    print(f'Seu email: {email} \nE valido')
else:
    print('Email invalido')