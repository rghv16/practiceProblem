length = int(input())
arr = list(map(int, input().split(' ')))
brr = list(map(int, input().split(' ')))

xw = 0
w = 0
for i in range(length):
    xw += arr[i]*brr[i]
    w += brr[i]
print('{0:.1f}'.format(xw/w))
