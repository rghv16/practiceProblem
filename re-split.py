regex_pattern = r"[,.]"	# Do not delete 'r'.
# https://www.hackerrank.com/challenges/re-split/problem
import re
print("\n".join(re.split(regex_pattern, input())))
