#!/bin/python3

import math
import os
import random
import re
import sys

def minTime(machines, goal):
    limit = goal * min(machines) + 2
    days = [0]*limit # 1 based index array
    for ele in machines:
        j = 1
        while j*ele < limit:
            days[j*ele] += 1
            j += 1
    s = 0
    for i in range(1, len(days)):
        s += days[i]
        if s >= goal:
            return i
    print(s,'s')
    return -1

if __name__ == '__main__':
    nGoal = input().split()
    n = int(nGoal[0])
    goal = int(nGoal[1])
    machines = list(map(int, input().rstrip().split()))
    ans = minTime(machines, goal)
    print(ans)

