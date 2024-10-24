# faca um programa que leia uma frase pelo teclado e mostre:
# quantas vezes a letra "a"
# em que posicao ela aparece a primeira vez
# em que posicao ela aparece a ultima vez

#meu

#frase = str(input('Digite uma frase: ')).strip()
#count = frase.count('a')
#primeiro = frase.find('a')
#ultimo = frase.rfind('a')
#print('A letra "A" aparece:', count,'vezes')
#print('A primeira letra "a" aparece no caracter:', primeiro)
#print('A ultima letra "a" aparece no caracter:', ultimo)

#professor

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posicao {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))