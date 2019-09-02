# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-set-add/problem
i = int(input())
st = set()
while i>0:
    i -= 1
    st.add(input())
print(len(st))

