# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0, n):
    odd = ''
    even = ''
    for i, ele in enumerate(input()):
        if i%2 == 0:
            even += ele
        else:
            odd += ele
    print('{} {}'.format(even, odd))
    #s = input()
    # print(s[::2], s[1::2])

