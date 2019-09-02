from fractions import Fraction
from functools import reduce


# https://www.hackerrank.com/challenges/reduce-function/problem
def product(fracs):
    t = Fraction( reduce( lambda x,y: x*y, [ele.numerator for ele in fracs])    ,reduce( lambda x,y: x*y, [ele.denominator for ele in fracs])    
    )
    return t.numerator, t.denominator
    #return 1, 2

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
