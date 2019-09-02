import numpy

# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
numpy.set_printoptions(legacy='1.13')
size= tuple(
        map(int, input().split(' '))
        )
print(numpy.eye(*size
    ,
        dtype=float)
    )
