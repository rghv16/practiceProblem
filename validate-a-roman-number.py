'''
I 1
V 5
x 10
l 50
c 100
d 500
m 1000
'''

regex_pattern = r"^(M{0,3})?(C?D|D?C{0,3}|CM)?(LX{1,3}|X{0,3}|X?L|X?C)?(I?X|I?V|V?I{1,3})?$"

import re
print(str(bool(re.match(regex_pattern, input()))))

'''
this problem is a good example for iterative development
i crosscheck with a package name roman on pip

import re
from roman import toRoman

checker = r"^(M{0,3})?(C?D|D?C{0,3}|C?M)?(LX{1,3}|X{0,3}|X?L|X?C)?(I?X|I?V|V?I{1,3})?$"

for i in range(1, 2001):
	print("{}, {}, {}".format(i, toRoman(i), bool(re.match(checker, toRoman(i)))))

# for i in range(10, 110):
# 	print(toRoman(i))
'''
