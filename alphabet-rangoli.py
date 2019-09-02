# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    # your code goes here
    #print(len('e-d-c-b-a-b-c-d-e')) 5 + 4 +4 +4
    import string
    st = string.ascii_lowercase[:size][::-1]
    l = [] # using memoziation
    width = size + 3*(size - 1)
    for i in range(size):
        s = '-'.join( st[:i] + st[:1+i][::-1])
        p = "{:-^{width}s}".format(s, width=width)
        print(p)
        l.append(p)
    l.pop()
    i = len(l)-1
    while i>-1:
        print(l[i])
        i -= 1

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
