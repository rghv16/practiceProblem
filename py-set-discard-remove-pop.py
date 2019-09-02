# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
N = int(input())
while N > 0:
    N -= 1
    p = input()
    if p == 'pop':
        s.pop()
    elif p.strip().split(' ')[0] == 'discard':
        s.discard(int(p.strip().split(' ')[1]))
    elif p.strip().split(' ')[0] == 'remove':
        s.remove(int(p.strip().split(' ')[1]))
print(sum(s))

