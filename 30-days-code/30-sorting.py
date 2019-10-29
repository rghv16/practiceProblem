import sys

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
swap = 0
for i in range(0, n):
    for j in range(0, i):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            swap += 1
print('Array is sorted in {} swaps.'.format(swap))
print('First Element: {}'.format(arr[0]))
print('Last Element: {}'.format(arr[n-1]))

