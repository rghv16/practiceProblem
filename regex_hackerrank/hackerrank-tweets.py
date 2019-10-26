import re

cnt = 0
for _ in range(int(input())):
    if bool(re.search('hackerrank', input(), re.I)):
        cnt += 1
print(cnt)
