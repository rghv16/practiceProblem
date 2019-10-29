#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    name = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        
        if emailID.endswith('@gmail.com'):
            name.append(firstName)
    name.sort()
    print(*name, sep="\n")

