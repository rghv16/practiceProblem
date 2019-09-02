# Enter your code here. Read input from STDIN. Print output to STDOUT
## https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem
import re 

for _ in range(int(input())):
    inp = input()
    inp1 = re.sub(r'(?<= )(&&)(?= )','and', inp)
    print(re.sub(r'(?<= )(\|\|)(?= )', 'or', inp1))

