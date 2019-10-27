# Enter your code here. Read input from STDIN. Print output to STDOUT

'''

<char><char><char><char><char><digit><digit><digit><digit><char>
'''


import re

PATTERN = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
if __name__ == '__main__':
    for _ in range(int(input())):
        if bool(re.search(PATTERN, input())):
            print('YES')
        else:
            print('NO')
