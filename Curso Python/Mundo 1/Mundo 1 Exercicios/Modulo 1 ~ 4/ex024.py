# crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome "SANTO"

#meu

cidade = str(input('Digite o nome da cidade: ')).strip()
separar = cidade.split()
print('O nome da cidade comeca com "Santo"? {}'.format('SANTO' in separar[0].upper()))

# professor

#cid = str(input('Nome da sua cidade: ')).strip()
#print(cid[:5].upper() == 'SANTO')