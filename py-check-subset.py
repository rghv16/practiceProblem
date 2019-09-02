# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-check-subset/problem
t = int(input())
while t>0:
    t -= 1
    input()
    a = set(map(int, input().strip().split(' ')))
    input()
    b = set(map(int, input().strip().split(' ')))
    print(a.issubset(b))


