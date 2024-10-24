# faca um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente
# Ex: Ana maria de souza xdd leech newbie
# primeiro = Ana
# ultimo = souza

#meu

#nome = str(input('Digite seu nome: '))
#separar = nome.split()
#first = separar[0]
#ultimo = separar[-1]
#print('O primeiro nome e:',first)
#print('O ultimo nome e:',ultimo)

# professor

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Prazer em te conhecer {}'.format(n))
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))
