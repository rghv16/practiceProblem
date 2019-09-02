# https://www.hackerrank.com/challenges/no-idea/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
q, l = map(int, input().strip().split())
que = list(map(int, input().strip().split(' ')))
A = set(map(int, input().strip().split()))
B = set(map(int, input().strip().split()))
hap = 0
for ele in que:
    if ele in A:
        hap += 1
    if ele in B:
        hap -= 1
print(hap)


