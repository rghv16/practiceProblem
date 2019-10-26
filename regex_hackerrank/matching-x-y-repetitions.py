# the {x, y} tool will match between x and y (both inclusion) repetitions of character/ character class /group

Regex_Pattern = r'^[0-9]{1,2}[a-zA-Z]{3,}\.{,3}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
