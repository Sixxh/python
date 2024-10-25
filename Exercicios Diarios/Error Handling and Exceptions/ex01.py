# Programa principal
try:
    n = int(input('Qual numero voce deseja dividir 100 por: '))
    divi = 100/n
except ZeroDivisionError:
    print('Nao e possivel dividir por 0')
except ValueError:
    print('Valor nao numerico digitado')
except Exception as e:
    print(f'O seguinte error ocorreu: {e}')
else:
    print(f'O resultado de {n} dividido por 100 e {divi}')
finally:
    print('Obrigado por utilizar nosso programa.')