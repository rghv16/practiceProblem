# Enter your code here. Read input from STDIN. Print output to STDOUT

# https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
my_queue = deque()

no_op = int(input())
while no_op>0:
    no_op -= 1
    inp = input()
    if any([ele.isdigit() for ele in inp]):
        
        command, value = inp.split()[0], int(inp.split()[1])
        getattr(my_queue, command)(value)
    else:
        command = inp.strip()
        getattr(my_queue, command)()

print(*my_queue, sep=' ')    

