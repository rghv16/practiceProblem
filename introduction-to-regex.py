# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re 
pat = re.compile(r'^[+-]?[0-9]*[.][0-9]+$')
test_case = int(input())
while test_case > 0:
    test_case -= 1
    print(bool(re.search(pat, input())))
        

