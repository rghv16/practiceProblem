# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem
from itertools import combinations

input()
tp = tuple(input().split(' '))
num = int(input())
with_a = 0
without_a = 0
for ele in combinations(tp, num):
    if 'a' in ele:
        with_a  += 1
    without_a += 1
print(with_a / without_a)

