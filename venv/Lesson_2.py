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
position = 0
find_string = string.find('abc', position)
while string.find('abc', position) != -1:  # find the substring
    print('the positions of the substring: ', string.find('abc', position))
    # find the position of the first sub string endless, so must+1
    position = string.find('abc', position) + 1  # find the position of the rest substrings if it has
