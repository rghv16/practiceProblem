# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-union/problem
input()
A = set(map(int, input().strip().split(' ')))
input()
B = set(map(int, input().strip().split(' ')))
print(len(A.union(B)))

