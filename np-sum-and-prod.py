import numpy
# https://www.hackerrank.com/challenges/np-sum-and-prod/problem
n, m = map(int, input().split(' '))
l = list()

for _ in range(m):
    l.append(list(map(int, input().split(' '))))

arr = numpy.array(l, dtype = int)
print(numpy.prod(numpy.sum(l, axis = 0)))



