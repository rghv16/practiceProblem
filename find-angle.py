# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/find-angle/problem
import math
AB = int(input())
BC = int(input())
print(str(int(round(math.degrees(math.atan2(AB,BC)))))+'°')

