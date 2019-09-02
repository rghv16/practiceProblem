import numpy
#numpy.set_printoptions(legacy='1.13')

## https://www.hackerrank.com/challenges/np-inner-and-outer/problem
l1 = list()
l2 = list()

l1.append(list(map(int, input().split())))
l2.append(list(map(int, input().split())))

arr1 = numpy.array(l1, dtype = int)
arr2 = numpy.array(l2, dtype = int)

print(numpy.inner(arr1, arr2)[0][0])
print(numpy.outer(arr1, arr2))

