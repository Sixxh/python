#pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
#pessoas['nome'] = 'Leandro'
#pessoas['peso'] = 98.5
#del pessoas['sexo']
#for k, v in pessoas.items():
#    print(f'{k} = {v}')

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0]['uf'])
#print(brasil[1]['sigla'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativas: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    #for k, v in e.items():
    #    print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
    print()