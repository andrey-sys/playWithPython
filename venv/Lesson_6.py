# while statement

# exercise_1
# Complete up to a hundred
print('Enter number not bigger than 100: ')
number = int(input())
while number<=100:
    print(number, end=' ')
    number=number+1
print('The end')

# exercise_2
# Find the maximum number value from the array
print('Enter any numbers, and in the end of the array set zero: ')
number=int(input())
maxNumber = number
while number!=0:
    number=int(input())
    if number!=0 and number>maxNumber: # if you change the sign up versa, you will get a smaller
                                       # number in the array
        maxNumber=number
print(maxNumber)

# exercise_3
# Count the sum of the array, to stop the array press zero and hit Enter button
number = int(input('Enter the number: '))
sumSeg = number
while number!=0:
    number = int(input('Enter the number: '))
    sumSeg+=number
print('There is a sum of your array: ', sumSeg)

# exercise_4
# find the substring
string = 'srfeabcvs desrg abc hoey abc'
position = 0
find_string = string.find('abc', position)
while string.find('abc', position) != -1:
    print('the positions of the substring: ', string.find('abc', position))
    # find the position of the first sub string endless, so must+1
    position = string.find('abc', position) + 1  # find the position of the rest
    # substrings if it has

# or we can simplify it
# find the position of your substring
print('Enter new string: ')
string = input()
print('Enter new substring: ')
substring = input()
position = string.find(substring)
while position!=-1:
    print('your positions: ',position)
    position=string.find(substring,position+1)

# exercise_5
# find & replace substring by another substring
print('Enter the phrase: ')
string = input()
print('What word do you want to replace? ')
sub_string = input()
print('Enter new word: ')
new_substring = input()
print(string.replace(sub_string,new_substring))

# exercise_6
# find & replace
print('Enter the phrase: ')
phrase = input()
print('Enter the sub phrase to replace: ')
sub_phrase=input()
print('Enter the new sub frase: ')
new_subphrase = input()
while phrase.find(sub_phrase)!=-1:
    phrase= phrase.replace(sub_phrase,new_subphrase)
    print(phrase)
