# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

Regex_Pattern = r'^[Hh][Ii]\s[^Dd]'
for _ in range(int(input())):
    inp = input()
    if bool(re.search(Regex_Pattern, inp)):
        print(inp)


