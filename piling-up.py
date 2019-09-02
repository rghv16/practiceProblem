# https://www.hackerrank.com/challenges/piling-up/problem
test_case = int(input())
while test_case > 0:
    test_case -= 1
    input()
    l = list(map(int, input().split(' ')))
    # two pointer approach
    i, j = 0, len(l) - 1
    can_done = True
    previous_pile_length = max(l[i], l[j])
    while i<j:
        if l[i] >= l[j]:
            if previous_pile_length >= l[i]:
                previous_pile_length = l[i]
                i +=1
            else:
                can_done = False
                break
        else:
            if previous_pile_length >= l[j]:
                previous_pile_length = l[j]
                j -= 1
            else:
                can_done = False
                break
    if can_done:
        print("Yes")
    else:
        print("No")

