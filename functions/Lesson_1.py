# functions

def print_text(string):
    return print(string)


def factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result


print(print_text('factorial of this number is: '), factorial(5))
