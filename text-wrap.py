import textwrap
import math


#https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    lst = ''
    p = len(string)
    i =0
    while i<p:
        lst = lst +string[i:min(i+max_width, p)] +'\n'
        i += max_width
    return lst

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
