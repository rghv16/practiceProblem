# https://www.hackerrank.com/challenges/itertools-product/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
A = list(map(int, input().strip().split(' ')))
B = list(map(int, input().strip().split(' ')))
print(*itertools.product(A, B))

