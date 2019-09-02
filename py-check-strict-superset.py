# Enter your code here. Read input from STDIN. Print output to STDOU
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem
A = set(map(int, input().strip().split(' ')))
t = int(input())
flag = True
while t>0:
    t -= 1
    B = set(map(int, input().strip().split(' ')))
    if not A.issuperset(B):
        flag = False
        break
print(flag)



