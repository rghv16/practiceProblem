#!/bin/python3
# https://www.hackerrank.com/challenges/most-commons/problem
from collections import Counter
if __name__ == '__main__':
    s = input()
    for ele in Counter(sorted(s)).most_common(3):
        print(ele[0], ele[1])

