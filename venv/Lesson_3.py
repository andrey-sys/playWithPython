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
print('the total cost of two parts is: ', (cost1 + cost2) // 100,'.' ,(cost1 + cost2) % 100)

