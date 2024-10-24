def check_age(age):
    if age < 18:
        raise ValueError('Usuario e menor de idade')
    else:
        print('Usuario Maior de idade')
    return age

# Programa principal
try:
    age = int(input('Idade: '))
    check_age(age)
except ValueError as e:
    print(f'Erro: {e}')
else:
    print('Validacao de idade concluida')
finally:
    print('Fim da verificacao.')