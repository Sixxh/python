galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por Favor, digite apenas M OU F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer Continuar ? [S/N]')).upper()[0]
        if resposta in 'SN':
            break
        print('Responda apenas S OU N')
    if resposta == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo tempos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A media de idade e de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p['nome']} ', end='')
print()
print(f'D) Lista das pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<< ENCERRADO >>')