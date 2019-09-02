# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    # your code goes here
    w = len('{0:b}'.format(number))
    w1 = len(str(number))
    for i in range(1, 1+ number):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=w ))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
