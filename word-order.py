# Enter your code here. Read input from STDIN. Print output to STDOUT

# https://www.hackerrank.com/challenges/word-order/problem
from collections import OrderedDict
my_dict = OrderedDict()
num = int(input())
while num>0:
    num -= 1
    key = input().strip()
    my_dict[key] = my_dict.get(key, 0) + 1
    #if not key in my_dict:
    #   my_dict[]
print(len(my_dict))
for ele in my_dict:
    print(my_dict[ele], end=' ')

