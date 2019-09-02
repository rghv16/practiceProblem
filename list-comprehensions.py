# https://www.hackerrank.com/challenges/list-comprehensions/problem
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    k = [
        [i, j, k]  
        for i in range(x+1) 
        for j in range(y+1) 
        for k in range(z+1) 
        if i+j+k != n
        ]
    print(k)
'''
    l = list()
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k == n:
                    continue
                l.append([i, j, k])
'''
