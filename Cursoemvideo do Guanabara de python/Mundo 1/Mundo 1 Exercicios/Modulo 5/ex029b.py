# professor
velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Voce excedeu o limite permitido que e de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Parabens siga sua viajem em seguranca')   