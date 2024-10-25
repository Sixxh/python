# lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
# tuplas sao imutaveis
# lanche[1] = 'refrigerante' nao funciona pq tupla e imutavel

# print(sorted(lanche)) == coloca a tupla em ordem

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posicao {cont}')

# for comida in lanche:
#     print(f'Eu vou comer {comida}')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posicao {pos}')

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# d = b + a
# print(c)
# print(d)
# print(sorted(c))
# print(sorted(d))
# print(c.count(5)) # conta quantos numeros 5 tem na tupla C
# print(c.index(8)) # mostra em qual posicao esta o primeiro numero 8
# print(c.index(5, 2)) # se colocar uma virgula vc consegue escolher a partir de qual posicao ele vai comecar a procurar para achar o primeiro numero 5 e ignora os anteriores

pessoa = ('Gustavo', 39, 'M', 99.88) # diferente de outras linguagens o python aceita diferentes tipo de dados
del(pessoa[0]) # n funciona deletar um elemento especifico pq a tupla e imutavel
del(pessoa) # usado para apagar qualquer variavel inclusive uma tupla
print(pessoa)