# Enter your code here. Read input from STDIN. Print output to STDOUT
## https://www.hackerrank.com/challenges/itertools-permutations/problem
import itertools
s, b= input().strip().split(' ')
for ele in sorted(itertools.permutations(s, int(b))):
    print(''.join(ele))
