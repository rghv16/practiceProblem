#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    cnt = 0
    for i in range(len(a)):
        for j in range(len(a) - i-1):
            if a[j+1] < a[j]:
                cnt += 1
                a[j+1], a[j] = a[j], a[j+1]
    ##print(a)
    print('Array is sorted in {} swaps.'.format(cnt))
    print('First Element: {}\nLast Element: {}'.format(a[0], a[-1]))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)

