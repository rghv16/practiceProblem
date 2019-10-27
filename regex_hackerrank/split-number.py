
import re

if __name__ == '__main__':
    pattern = r'^([0-9]{1,3})[- ]([0-9]{1,3})[- ]([0-9]{4,10})$'

    for _ in range(int(input())):
        match = re.search(pattern, input())
        print("CountryCode={},LocalAreaCode={},Number={}".format(match.group(1), match.group(2), match.group(3)))
        #print(match)
