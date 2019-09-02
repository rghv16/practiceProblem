import re

# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem
pattern = re.compile(
    r'^<([a-zA-Z][a-zA-Z0-9_.-]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})>$'
    )
for _ in range(int(input())):
    a,b = input().split(' ')
    m = re.search(pattern, b)
    if m:
        print(a, b)


