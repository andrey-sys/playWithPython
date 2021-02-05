# if & elif statements

# exercise_1
# set any number and turn it to positive number
print('Enter any number: ')
number = int(input())
if number >= 0:
    print(number)
else:
    print(-number)

# exercise_2
# find the biggest number between two numbers
print('Enter first number')
a = int(input())
print('Enter second number')
b = int(input())
if a >= b:
    print(a)
else:
    print(b)

# exercise_3
# find the quarter of coordinates
print('Enter X coordinate')
x = int(input())
print('Enter Y coordinate')
y = int(input())
if x > 0:
    if y > 0:
        print('There is first quarter')
    else:
        print('There is forth quarter')
else:
    if y > 0:
        print('There is second quarter')
    else:
        print('There is third quarter')

# exercise_4
# convert 1,2,3 to words, for other print Other
print('Enter the number')
number = int(input())
if number == 1:
    print('One')
elif number == 2:
    print('Two')
elif number == 3:
    print('Three')
else:
    print('Other number')
