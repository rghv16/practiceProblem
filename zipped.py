# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/zipped/problem
student_num, subject_num = map(int, input().split())
l = list()
for _ in range(subject_num):
    l.append(tuple(map(float, input().split(' '))))
for ele in zip(*l):
    print(sum(ele) / subject_num)



