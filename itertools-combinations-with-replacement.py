# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
from itertools import combinations_with_replacement
st, num = input().strip().split(' ')
num = int(num)
for ele in combinations_with_replacement(sorted(st), num):
    print(''.join(ele))

