n = int(input())
d = {}
for i in range(0, n):
    key, value = input().split()
    d[key] = int(value)
for i in range(0, n):
    key = input()
    if key in d:
        print('{}{}{}'.format(key,'=',d[key]))
    else:
        print('Not found')
