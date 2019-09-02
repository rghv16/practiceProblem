#!/bin/python3

## https://www.hackerrank.com/challenges/matrix-script/problem
import math
import os
import random
import re
import sys

pattern = re.compile(r'(?<=[a-zA-Z0-9])[ !@#$%&]+(?=[a-zA-Z0-9])')

def mat_to_str(matrix):
    row = len(matrix)
    column = len(matrix[0])
    st = ''
    for i in range(column-1, -1, -1):
        for j in range(row-1, -1 , -1):
            st = matrix[j][i] + st
    m = re.sub(pattern, ' ', st)
    print(m, end='')

nm = input().split()
n = int(nm[0])
m = int(nm[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
mat_to_str(matrix)

