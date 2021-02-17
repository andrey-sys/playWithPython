#conditions <= >= < > ==

# exercise_1
# if number is even or not
print('Enter any number')
number = int(input())
isEven = number % 2 == 0
print(isEven)

# exercise_2
# if two lines have a crosspoint
print('Enter beginning of the first line')
startFirstLine = int(input())
print('Enter ending of the first line')
finishFirstLine = int(input())
print('Enter beginning of the second line')
startSecondLine = int(input())
print('Enter ending of the second line')
finishSecondLine = int(input())
ifStartFirstLineInSecond = startSecondLine<=startFirstLine<= finishSecondLine
ifFinishFirstLineInSecond = startSecondLine<=finishFirstLine<=finishSecondLine
ifStartSecondLineInFirst = startFirstLine<=startSecondLine<=finishFirstLine
ifFinishSecondLineInFirst = startFirstLine <= finishSecondLine<= finishFirstLine
theAnswer=ifStartFirstLineInSecond or ifFinishFirstLineInSecond or\
          ifStartSecondLineInFirst or ifFinishSecondLineInFirst
print('The answer is : ',theAnswer,  '  ->if you get "true" you have the crossline, '
                                    'if you get "false" you have not the crossline' )

#or simplify it in one row
theAnswerSimplified = startFirstLine<=finishSecondLine and startSecondLine <= finishFirstLine
print('The answer is : ',theAnswerSimplified,  '  ->if you get "true" you have the crossline, '
                                    'if you get "false" you have not the crossline' )