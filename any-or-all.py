# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/any-or-all/problem
num = int(input())
tup = tuple(input().split(' '))
print(
    all( int(ele) > 0 for ele in tup)
    and 
    any( ele== ele[-1::] for ele in tup)
)

