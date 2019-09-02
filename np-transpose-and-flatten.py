import numpy
# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
row, column = map(int, input().split(' '))
l = list()
for _ in range(row):
    l.append(list(map(int, input().split(' '))))
Arr = numpy.array(l)
print(numpy.transpose(Arr))
print(Arr.flatten())




