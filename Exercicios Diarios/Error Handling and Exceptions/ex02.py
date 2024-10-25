def check_age(age):
    if age < 18:
        raise ValueError('Usuario e menor de idade')
    else:
        print('Usuario Maior de idade')
    return age

age = int(input('Idade: '))
check_age(age)