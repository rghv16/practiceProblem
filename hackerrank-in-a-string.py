#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    sub_string = 'hackerrank'
    sub_index = 0
    for ele in s:
        if ele == sub_string[sub_index]:
            sub_index += 1
            if sub_index == len('hackerrank'):
                break
    return 'YES' if sub_index == len('hackerrank')  else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        fptr.write(result + '\n')
    fptr.close()

