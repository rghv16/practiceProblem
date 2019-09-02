# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/incorrect-regex/problem
import re
test = int(input())
while test>0:
    test -= 1
    inp = input()
    try:
        re.compile(inp)
        print("True")
    except BaseException as e:
        print("False")

