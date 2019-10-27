'''
rules are simple enough
Print 1 if the conversation starts with hackerrank
Print 2 if the conversation ends with hackerrank
Print 0 if the conversation starts and ends with hackerrank
Print -1 if none of the above.
'''
import re

PATTERN = re.compile(r'hackerrank')
if __name__ == '__main__':
    for _ in range(int(input())):
        inp = input()
        for match in PATTERN.finditer(inp):
            if match.start() == 0:
                if match.end() == len(inp):
                    print("0")
                else:
                    print("1")
            elif match.end() == len(inp):
                print("2")
            else:
                print("-1")

