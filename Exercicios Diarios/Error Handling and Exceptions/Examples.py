def check_positive_number(num):
    # Raising Exceptions Manually
    # You can manually raise an exception using the {raise} keyword. This is useful when you want to signal that an error has occurred, even if the Python interpreter hasn't caught it yet.
    if num < 0: # checka se o numero eh negativo
        # \/ alerta manualmente que se for negativo eh um error
        raise ValueError("The number must be positive.") 
    return num

# You can create your own exception classes by subclassing Python’s built-in Exception class. This is helpful when you need more specific error types that are not covered by Python's standard exceptions.

class InvalidAgeError(Exception):
    pass # Quando uma condição externa é acionada, a instrução pass permite lidar com a condição sem que o loop seja impactado; todo o código continuará sendo lido a menos que um break ou outra instrução ocorra 
    # A instrução pass dizendo ao programa para continuar executando e ignorar o fato de que a variável number é avaliada como equivalente a 5 durante uma das iterações.
def validate_age(age):
    if age < 0:
        raise InvalidAgeError('Age cannot be negative.')


# You can catch multiple exceptions using a singel {except} block or separate them into different blocks to handle them differently.
try:
    # code that might riase multiple esceptions
    x = int(input('Enter a number: '))
    result = 10 / x
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occured: {e}')
   

# You can use a {try} block inside another {try} block for more granular error handling. this is useful when you want to catch specific errors in different parts of your code.
try:
    try:
        result = 10/0
    except ZeroDivisionError:
        print('Inner: Cannot divide by zero.')
except:
    print('Outer: An error ocurred')