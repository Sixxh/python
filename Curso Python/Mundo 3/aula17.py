# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7) # adicionar elemento ao final da lista
# num.sort(reverse=True) # coloca a lista em ordem contraria [9 5 2 1]
# num.insert(2, 2) # insere um valor extra na posicao escolhida(2) 
# num.pop() # se n especificar o elemento a ser deletado ele deleta o ultimo elemento
# num.remove(2) # procura do inicio da lista a primeira ocorrencia do valor especificado para eliminar e elimina
# if 4 in num:
#     num.remove(4)
# else:
#     print('Nao achei o numero 4.')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')
# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for cont in range(0, 3):
#     valores.append(int(input('Digite um valor: ')))
# 
# for c, v in enumerate(valores): # se quiser saber o indice dos valores usar enumerate
#     print(f'Na posicao {c} encontrei os valores {v}...')
a = [2, 3, 4, 7]
b = a # isso cria uma ligacao entre a e b por isso a alteracao para o numero 8 acontece nas 2 listas
c = a[:] # isso cria uma copia da lista a por isso a alteracao de valores so ocorre nessa lista
b[2] = 8
c[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')