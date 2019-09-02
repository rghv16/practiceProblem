# https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    l = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append((name, score))
    l.sort(key = lambda x:x[1])
    item = l[0]
    value = 0
    for ele in l:
        if ele[1] == item[1]:
            continue
        value = ele[1]
        break
    p = []
    for ele in l:
        if ele[1] == value:
            p.append(ele[0])
    p.sort()
    for ele in p:
        print(ele)

