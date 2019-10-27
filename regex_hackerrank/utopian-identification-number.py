'''


'''


import re

PATTERN = r'^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$'
if __name__ == '__main__':
    for _ in range(int(input())):
        if bool(re.search(PATTERN, input())):
            print('VALID')
        else:
            print('INVALID')
