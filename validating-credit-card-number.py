# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re
pattern = re.compile(r"^[456]\d\d\d-?\d\d\d\d-?\d\d\d\d-?\d\d\d\d$")
pattern1 = re.compile(r'(\d)\1\1\1')


for _ in range(int(input())):
    inp = input()
    m = pattern.match(inp)
    inp = inp.replace('-','')
    m1 = pattern1.search(inp)
    if m1 == None and m:
        print("Valid")
    else:
        print("Invalid")


