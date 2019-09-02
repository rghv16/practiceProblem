# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/maximize-it/problem
import itertools

t, mod = map(int, input().strip().split(' '))
l = list()
while t>0:
    t -= 1
    l.append(tuple( map( lambda x:x%mod, map( lambda x:x**2, map(int , input().split(' ')[1:])))))

#print(*itertools.product(*l))
#print(*l, sep="\n")
print(max(map(lambda x:sum(x)%mod, itertools.product(*l))))

