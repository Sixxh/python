from ex107a import moedas

p = float(input('Digite o preco: R$ '))
print(f'A metade de {p} e {moedas.metade(p)}')
print(f'O dobro de {p} e {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moedas.diminuir(p, 13)}')