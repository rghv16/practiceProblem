# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem
import re
pattern = re.compile(r'^[789][0-9]{9}$')
for _ in range(int(input())):
    m = re.match(pattern, input())
    print("YES" if m else "NO")

