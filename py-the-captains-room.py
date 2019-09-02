# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-the-captains-room/problem
d = {}
grp = int(input())
for ele in map(int, input().strip().split(' ')):
    d[ele] = d.get(ele, 0) + 1
e = None
for ele in d:
    if d[ele] == 1:
        e = ele
print(e)

