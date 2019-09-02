#!/bin/python3

# https://www.hackerrank.com/challenges/py-if-else/problem
N = int(input())
if N%2 == 1:
    print("Weird")
elif N <= 5 and N >= 2:
    print("Not Weird")
elif N <= 20 and N >= 6:
    print("Weird")
else:
    print("Not Weird")

