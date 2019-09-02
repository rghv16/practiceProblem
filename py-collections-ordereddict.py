# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
my_dict = OrderedDict()
num = int(input())
while num>0:
    num -= 1
    inp = input().split()
    item_name, price = ' '.join(inp[0:-1]), int(inp[-1])
    if not item_name in my_dict:
        my_dict[item_name] = price
    else:
        my_dict[item_name] += price
for ele in my_dict:
    print(ele, my_dict[ele])

