# functions

# exercise_1
def print_text(s):
    return print(s)


def factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result


print_text('Enter any number: ')
n = int(input())
print_text('Your factorial is: ')
print(factorial(n))
