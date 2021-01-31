print('exercise 1')
print('enter number of pupils: ')
N = int(input())
print('enter number of apples: ')
K = int(input())
print('how many apples get any of the people?')
print('answer is: ', K // N, ' apples will get each of the pupils')

print('exercise 2')
print('enter dollar price: ')
a = int(input())
print('enter cent price: ')
b = int(input())
print('enter dollar price: ')
c = int(input())
print('enter cent price: ')
d = int(input())
cost1 = a * 100 + b
cost2 = c * 100 + d
print('the total cost of two parts is: ', (cost1 + cost2) // 100, '.', (cost1 + cost2) % 100)

print('exercise 3')
print('enter 2 number, the first number is any number, and the second number''\n'
      ' for cutting the last number or several numbers, how many you want to cut.''\n'' '
      'For exaple: first num is 12345, and you want to cut '
      'last 2, so you need enter the second number "2"')
the_number = int(input())
cut_the_end = int(input())
print(the_number // 10 ** cut_the_end)

print('exercise 4')
print('Rounding up for define two numbers.''\n'''
      'for example 13/3 = 5')
print('Enter two number:')
a = int(input())
b = int(input())
print((a + b - 1) // b)
# or another way but same rusult
print((a - 1) // b + 1)

print('exercise 5')
print('enter 3 number, first 2 numbers is a price in dollar and cents''\''
      'third number is quantity of apples')
print('enter dollar price: ')
dollar = int(input())
print('enter cent price: ')
cents = int(input())
print('enter quantity of apples: ')
quantity_of_apples = int(input())
dollar_to_cents = (dollar * 100)
print('the total cost of aplles is: ', ((dollar_to_cents + cents) * quantity_of_apples) // 100, '.',
      ((dollar_to_cents + cents) * quantity_of_apples) % 100)
