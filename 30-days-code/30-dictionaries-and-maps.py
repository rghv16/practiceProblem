n = int(input())
d = {}
for i in range(0, n):
    key, value = input().strip().split()
    d[key] = value


while True:
    try:
        key = input().strip()
        if key in d:
            print('{}{}{}'.format(key,'=',d[key]))
        else:
            print('Not found')
    except:
        break
