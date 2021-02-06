# Data types and output functions
expression = '10 + 10 = '
answer = 10 + 10
print(expression + str(answer))

print('  Creativaty, Imegination, Strategy  ' * 3)  # 5 dog

print('Enter any frase of Benjamin Disraeli: ')
phrase = input()
print(phrase)
print('      Benjamin Disraeli')

print('enter number from 0 to 10, to multiply it')
a = int(input())
print('enter again number from 0 to 10, to multiply it')
b = int(input())
print('your answer')
print(a * b)

print(int('100' * 100) ** 2)  # without int wouldn't work

word = 'Bye'
phrase = word * 3 + '!'
print(phrase)

print('Enter any number for getting remainder')
n = int(input())
print(n % 256)

print('Enter any number not lower than 100: you will get the root of the number')
number = int(input())
print(2 ** number)

n = 111
a = n // 100
k = n % 100
b = k // 10
c = k % 10
print(a + b + c)
