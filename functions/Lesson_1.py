# functions

# exercise_1
# count the factorial
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


# exercise_2
# find the biggest number between three numbers, and use 2 functions
def find_max(a, b):
    if a > b:
        return a
    return b


print_text('The max number is: ')
print_text(find_max(4, 50))
