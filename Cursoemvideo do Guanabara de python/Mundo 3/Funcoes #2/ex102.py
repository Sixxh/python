# crie um programa que tenha uma funcao factorial() que receba dois parametros: o primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico(opcional) indicado se sera mostrado ou nao na tela o processo de calculo do fatorial.

def factorial(num, show=False):
    """-> Calcula o factorail de um numero.
        :param num: O numero a ser calculado.
        :param show: (opcional) Mostrar ou nao a conta.
        :return: O valor do factorial de um numero n."""
    fac = 1
    if show == False:
        for c in range(num, 0, -1):
            fac *= c
        return fac
    elif show:
        for c in range(num, 0, -1):
            fac *= c
            if c != 1:
                print(f' {c} x', end='')
            else:
                print(f' {c}', end='')
        return f' = {fac}'


#Programa principal
print(factorial(5, True))