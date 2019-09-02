import numpy

# https://www.hackerrank.com/challenges/np-concatenate/problem
n, m, p = map(int, input().split(' '))
l1 = list()
l2 = list()
for _ in range(n):
    l1.append(list(map(int, input().split(' '))))

for _ in range(m):
    l2.append(list(map(int, input().split(' '))))

print(numpy.concatenate((numpy.array(l1), numpy.array(l2)), axis = 0))


