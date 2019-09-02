# https://www.hackerrank.com/challenges/python-sort-sort/problem

row, no_ele = map(int, input().split())
l = list()

for _ in range(row):
    l.append(tuple(map(int, input().split(' '))))
k = int(input())
for ele in sorted(l,key = lambda x:x[k]):
    print(*ele)
