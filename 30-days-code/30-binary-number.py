#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr = bin(n)[2:]

    i = 0
    length = len(arr)
    mx  = 0
    
    while i<length:
        cur = 0
        while i<length and arr[i] == '1':
            cur += 1
            i += 1
        mx = max(mx, cur)
        i += 1
    print(mx)
