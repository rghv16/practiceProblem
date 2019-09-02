import numpy

# https://www.hackerrank.com/challenges/np-linear-algebra/problem
numpy.set_printoptions(legacy='1.13')
row = int(input())
l1 = list()

for _ in range(row):
    l1.append(list(map(float, input().split())))


arr1 = numpy.array(l1, dtype = float)

print(numpy.linalg.det(l1))
#print(numpy.cross(arr1, arr2))



