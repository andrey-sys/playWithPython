# # while statement
#
# # exercise_1
# # Complete up to a hundred
# print('Enter number not bigger than 100: ')
# number = int(input())
# while number<=100:
#     print(number, end=' ')
#     number=number+1
# print('The end')
#
# # exercise_2
# # Find the maximum number value from the array
# print('Enter any numbers, and in the end of the array set zero: ')
# number=int(input())
# maxNumber = number
# while number!=0:
#     number=int(input())
#     if number!=0 and number>maxNumber: # if you change the sign up versa, you will get a smaller
#                                        # number in the array
#         maxNumber=number
# print(maxNumber)

# # exercise_3
# # Count the sum of the array, to stop the array press zero and hit Enter button
# number = int(input('Enter the number: '))
# sumSeg = number
# while number!=0:
#     number = int(input('Enter the number: '))
#     sumSeg+=number
# print('There is a sum of your array: ', sumSeg)

# exercise_4
# find the substring
string = 'srfeabcvs desrg abc hoey abc'
position = 0
find_string = string.find('abc', position)
while string.find('abc', position) != -1:
    print('the positions of the substring: ', string.find('abc', position))
    # find the position of the first sub string endless, so must+1
    position = string.find('abc', position) + 1  # find the position of the rest substrings if it has
