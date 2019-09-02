import numpy


# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
numpy.set_printoptions(legacy='1.13')
row = int(input())
l1 = list()
l2 = list()

for _ in range(row):
    l1.append(list(map(int, input().split())))

for _ in range(row):
    l2.append(list(map(int, input().split())))

arr1 = numpy.array(l1, dtype = int)
arr2 = numpy.array(l2, dtype = int)

print(numpy.dot(arr1, arr2))
#print(numpy.cross(arr1, arr2))

