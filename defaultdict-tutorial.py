# Enter your code here. Read input from STDIN. Print output to STDOUT
## https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict
my_dict = defaultdict(list)
A, B = map(int, input().strip().split(' '))
i = 1
while A>0:
    A -= 1
    my_dict[input()].append(i)
    i += 1

while B>0:
    B -= 1
    querry = input()
    if len(my_dict[querry]) == 0:
        print("-1")
    else:
        print(*my_dict[querry], sep=' ')



