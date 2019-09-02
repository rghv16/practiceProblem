## https://www.hackerrank.com/challenges/python-lists/problem
if __name__ == '__main__':
    N = int(input())
    l = list()
    while N > 0:
        N -= 1
        inp = input()
        if 'insert' in inp:
            inp = inp.strip().split(' ')
            index, value = int(inp[1]), int(inp[2])
            l.insert(index, value)
        elif 'print' in inp:
            print(l)
        elif 'remove' in inp:
            value = int(inp.strip().split(' ')[1])
            l.remove(value)
        elif 'append' in inp:
            value = int(inp.strip().split(' ')[1])
            l.append(value)
        elif 'sort' in inp:
            l.sort()
        elif 'pop' in inp:
            l.pop()
        elif 'reverse' in inp:
            l.reverse()
    



