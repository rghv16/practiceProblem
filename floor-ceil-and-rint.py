import numpy
# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem
numpy.set_printoptions(legacy='1.13')
arr1 = numpy.array(input().split(' '), dtype=float)

print(numpy.floor(arr1))
print(numpy.ceil(arr1))
print(numpy.rint(arr1))

