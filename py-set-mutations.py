# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-mutations/problem
input()
A = set(map(int, input().strip().split(' ')))
N = int(input().strip())
while N>0:
    N -= 1
    p = input()
    if p.split(' ')[0] == 'intersection_update':
        s = set(map(int, input().strip().split(' ')))
        A.intersection_update(s)
        #print('m1', len(A))

    elif p.split(' ')[0] == 'update':
        s = set(map(int, input().strip().split(' ')))
        A.update(s)
        #print('m2', len(A))

    elif p.split(' ')[0] == 'symmetric_difference_update':
        s = set(map(int, input().strip().split(' ')))
        A.symmetric_difference_update(s)
        ##print('m3', len(A))

    else:
        s = set(map(int, input().strip().split(' ')))
        A.difference_update(s)
        #print('m4', len(A))

print(sum(A))
        


