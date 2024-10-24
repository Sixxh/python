def factorial(n, show=False):
    """-> Calcula o factorail de um numero.
        :param num: O numero a ser calculado.
        :param show: (opcional) Mostrar ou nao a conta.
        :return: O valor do factorial de um numero n."""
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Programa Principal
print(factorial(5, True))