## https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
import re
for ele in re.finditer(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeoiu]{2,})(?=[qwrtypsdfghjklzxcvbnm])',input(), flags = re.I):
        print(ele.group() if ele else -1)
'''
aa
aa
aa
aae
EAEOUOIou
'''

