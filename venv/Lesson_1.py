# Variables and arithmetic expressions
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
print(distance)

#exercise_1
# answer the quations
dateOfBirth = input('Enter your date of birth: ')
currenYear = input('Enter the current year: ')
yourAge  = int(currenYear) - int(dateOfBirth)
print('Your age is: ',yourAge)