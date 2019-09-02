# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem
from collections import namedtuple
num = int(input())
Student = namedtuple('Student',input())
l = list()

while num>0:
    num -= 1
    l.append(Student._make(input().split()))


s = 0
for ele in l:
    s += int(ele.MARKS)
print(s/len(l))

