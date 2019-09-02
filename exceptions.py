# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/exceptions/problem
num = int(input())
while num >0:
    num -= 1
    try:
        inp = input().split()
        a, b = map(int, inp)
        print(a //b)
    except BaseException as e:
       print("Error Code:",e )
