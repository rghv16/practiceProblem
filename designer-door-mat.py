
# https://www.hackerrank.com/challenges/designer-door-mat/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    lst = []
    #str.center(width, fillchar)
    row, height = map(int, input().split(' '))
    for i in range(row // 2):
        st = ('.|.'*(2*i+1)).center(height, '-')
        print(st)
        lst.append(st)
    print('WELCOME'.center(height, '-'))
    p = len(lst)
    while p>0:
        p -= 1
        print(lst.pop())

