from collections import Counter
length = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()
c = Counter(arr)


print(sum(arr) / length)

if length %2 == 0:
    print((arr[length // 2] + arr[length // 2 - 1]) / 2)
else:
    print(arr[(length + 1) // 2])

print(c.most_common(1)[0][0])
