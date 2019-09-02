# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/itertools-combinations/problem
import itertools


st, r = input().strip().split(' ')
r = int(r)

for i in range(1, r + 1):
    for ele in itertools.combinations(sorted(st), i):
        print(''.join(ele))
