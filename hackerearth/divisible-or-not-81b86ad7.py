
N = int(input())
data = [int(x) for x in input().split()]


# Write your code here
ans = data[-1]%10 == 0

print('Yes' if ans else 'No')
