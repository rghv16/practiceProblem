import re

PATTREN = r'^(\.|,|_)[0-9]+[a-zA-Z]*_?$'


for _ in range(int(input())):
    inp = input()
    if bool(re.search(PATTREN, inp)):
        print('VALID')
    else:
        print('INVALID')
