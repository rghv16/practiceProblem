import math


def is_prime(n):
    if n == 1:
        return 'Not prime'
    if n == 2 or n== 3 or n == 5:
        return 'Prime'
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        return 'Not prime'
    flag = True
    for i in range(2, math.ceil(math.sqrt(n)) +1):
        if n%i == 0:
            flag = False
            break
    if flag:
        return 'Prime'
    else:
        return 'Not prime'
    

if __name__ == '__main__':
    test_case = int(input())
    for _ in range(test_case):
        print(is_prime(int(input())))
        # num = int(input())
        # flag = True
        # for i in range(2, num//2 +2):
        #     if num%i == 0:
        #         flag = False
        #         break
        # if flag and num > 1:
        #     print('Prime')
        # else:
        #     print('Not prime')
        

