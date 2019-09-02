import numpy

# https://www.hackerrank.com/challenges/np-array-mathematics/problem
n, m = map(int, input().split(' '))
l1 = list()
l2 = list()
for _ in range(n):
    l1.append(list(map(int, input().split(' '))))

for _ in range(n):
    l2.append(list(map(int, input().split(' '))))
arr1 = numpy.array(l1)
arr2 = numpy.array(l2)

print(numpy.add(arr1, arr2))
print(numpy.subtract(arr1, arr2))
print(numpy.multiply(arr1, arr2))
print( arr1 // arr2)
#print(numpy.divide(arr1, arr2))
print(numpy.mod(arr1, arr2))
print(numpy.power(arr1, arr2))



