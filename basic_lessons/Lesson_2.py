# Data types and output functions
expression = '10 + 10 = '
answer = 10 + 10
print(expression + str(answer))

print('  Creativaty, Imegination, Strategy  ' * 3)  # 5 dog

print('Enter any frase of Benjamin Disraeli: ')
phrase = input()
print(phrase)
print('      Benjamin Disraeli')

#exercise_0
print('multiply two numbers')
print('enter number from 0 to 10, to multiply it')
a = int(input())
print('enter again number from 0 to 10, to multiply it')
b = int(input())
print('your answer')
print(a * b)

print('print square of 100*100**2')
print(int('100' * 100) ** 2)  # without int wouldn't work

word = 'Bye'
phrase = word * 3 + '!'
print(phrase)

print('Enter number bigger then 256 for getting remainder')
n = int(input())
print('your remainder is',n % 256)

print('Enter number that represent square for number 2')
number = int(input())
print(2 ** number)

n = 111
a = n // 100
k = n % 100
b = k // 10
c = k % 10
print(a + b + c)

# exercise_1
# playing with strings
string = 'abcdef'
print(string[2])  # represent third letter of the string
print(len(string))  # represent length of the string
print(string[-2])  # represent second letter from the end of the string
print(string[0:3])  # represent three first letter of the string
print(string[2:])  # represent string without 2 first characters
print(string[::2])  # represent even characters of the string or each second chracter
print(string[1::2])  # represent three odd characters of the string

# exercise_2
# methods find & replace
print('methods find & replace:')
string = 'srfeabcvs desrg abc hoey abc'
print(string.find('abc'))  # looking for substring "abc" the first one, and show the place of this
# substring in the main string
