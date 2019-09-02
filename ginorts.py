# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
## https://www.hackerrank.com/challenges/ginorts/problem
s = string.ascii_lowercase + string.ascii_uppercase + '13579'+'02468'
print(''.join(sorted(input(), key= s.index)))

