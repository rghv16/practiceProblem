# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/collections-counter/problem
import collections
input()
myCnt= collections.Counter(map(int, input().strip().split(' ')))
#print(myCnt)
t = int(input())
total_price = 0
while t>0:
    t -= 1
    size, price = map(int, input().strip().split(' '))
    if myCnt[size] > 0:
        myCnt[size] -= 1
        total_price += price
print(total_price)

