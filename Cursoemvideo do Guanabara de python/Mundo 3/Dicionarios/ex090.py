tudo = dict()
tudo['Nome'] = str(input('Nome: '))
tudo['Media'] = float(input(f'Media de {tudo["Nome"]}: '))
if tudo['Media'] >= 5:
    tudo['Situacao'] = 'Aprovado'
else:
    tudo['Situacao'] = 'Reprovado'
for n, m in tudo.items():
    print(f'{n} e igual a {m}')