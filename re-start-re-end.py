# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/re-start-re-end/problem
import re 
s = input()
k = input()
pattern = re.compile(k)
m = pattern.search(s)
if m == None:
    print('(-1, -1)')
else:
    while m != None and m.end() <= len(s):
        print('({0}, {1})'.format(m.start(), m.end()-1))
        m = pattern.search(s, m.start() + 1)

    

