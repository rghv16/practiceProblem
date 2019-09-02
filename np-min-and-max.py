import numpy

# https://www.hackerrank.com/challenges/np-min-and-max/problem
n, m = map(int, input().split(' '))
l = list()

for _ in range(n):
    l.append(list(map(int, input().split(' '))))

arr1 = numpy.array(l, dtype = int)
print(numpy.max(numpy.min(arr1, axis = 1), axis = 0))



