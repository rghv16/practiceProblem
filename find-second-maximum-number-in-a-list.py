# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    t_runner = tuple(arr)
    first_max = -200
    second_max = -200
    for ele in t_runner:
        first_max = max(first_max, ele)
    for ele in t_runner:
        if ele == first_max:
            continue
        second_max = max(second_max, ele)
    print(second_max)


