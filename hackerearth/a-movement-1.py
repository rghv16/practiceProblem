'''
after repetitive divison of 5
only 1 step is needed
'''
num = int(input())

a = num//5

if num%5 != 0:
    a += 1

print(a)
