## https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
A = set(map(int, input().strip().split(' ')))
input()
B = set(map(int, input().strip().split(' ')))

l = list()
l.extend(A.difference(B))
l.extend(B.difference(A))
l.sort()
print(*l,sep = '\n')


