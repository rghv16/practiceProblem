import numpy

# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
numpy.set_printoptions(legacy='1.13')
row, col = map(int, input().split(' '))
l = list()
for _ in range(row):
    l.append(list(map(int, input().split(' '))))

arr1 = numpy.array(l, dtype = int)
print(numpy.mean(arr1, axis=1))
print(numpy.var(arr1, axis=0))
print(numpy.std(arr1, axis=None))



