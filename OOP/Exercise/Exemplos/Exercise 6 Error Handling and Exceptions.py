try:
    # cod ethat might raise an exception
    result = 10 / 0 # this will riase a ZeroDivisionError
except ZeroDivisionError:
    # this block executes if a ZeeroDivisionError occurs
    print("You can't divide by zero!")
except Exception as e:
    # this block chatches any other exceptions
    print(f'An error ocurred: {e}')
finally:
    print('This will alwasy run')