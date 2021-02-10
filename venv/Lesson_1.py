# Variables and arithmetic expressions
from math import floor, ceil, sqrt

print('10', '20', '30', "40", sep='+', end=' ')
print('=', 10 + 20 + 30 + 40)
print(20 % 3, "returns remainder")
print(20 // 3, "returns integer division")
print(20 ** 3, "returns root of 3")
print("instance for a clock ", (23 - 8) % 24)
print()
speed = 108
time = 2
distance = speed * time
time = distance / speed
print(distance, 'km ', speed, 'km\h ', time, 'hour ', sep='')

# exercise_1
# answer the quations
dateOfBirth = input('Enter your date of birth: ')
currenYear = input('Enter the current year: ')
yourAge = int(currenYear) - int(dateOfBirth)
print('Your age is: ', yourAge)

# exercise_2
# some float expressions
print('{0:.10f}'.format(1.125))  # represent format & quantity of numbers after point
print(0.125.as_integer_ratio())  # represent common fraction
print(float(2 ** 10).as_integer_ratio())  # represent common fraction
print(int(2.5), int(3.5), int(-3.5))  # round to integer
print(round(2.5), round(3.5), round(-2.5))  # simple round
print(ceil(2.5), ceil(3.5), ceil(-2.5))  # round up
print(floor(2.5), floor(3.5), floor(-2.5))  # round down
print(sqrt(144))  # square root of 144
