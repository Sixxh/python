# desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso
# entre 18.5 e 25: peso ideal
# 25 ate 30: sobrepeso
# 30 ate 40: obesidade
# acima de 40: obesidade morbida
alt = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('Seu IMC e {:.2f} e voce esta abaixo do peso'.format(imc))
elif imc < 25:
    print('Seu IMC e {:.2f} e voce esta no seu peso ideal'.format(imc))
elif imc < 30:
    print('Seu IMC e {:.2f} e voce esta com sobrepeso'.format(imc))
elif imc < 40:
    print('Seu IMC e {:.2f} e voce esta com obesidade'.format(imc))
elif imc >= 40:
    print('Seu IMC e {:.2f} e voce esta com obesidade morbida'.format(imc))