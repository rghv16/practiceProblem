# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/validating-uid/problem

'''
It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits
It should only contain alphanumeric characters
No character should repeat.
There must be exactly 10 characters in a valid UID.
'''

import re
# i will use group for the 
pattern1 = re.compile(r'[A-Z]')
pattern2 = re.compile(r'[0-9]')
pattern3 = re.compile(r'[A-Za-z0-9]+')
pattern4 = re.compile(r'(.).*\1')

for _ in range(int(input())):
    inp = input()
    m4 = re.findall(pattern4, inp)
    m3 = pattern3.match(inp)
    m2 = re.findall(pattern2, inp)
    m1 = re.findall(pattern1, inp)
    if m3.end() == 10 and len(m1) > 1 and len(m2) > 2 and len(m4) == 0:
        print("Valid")
    else:
        print("Invalid")



