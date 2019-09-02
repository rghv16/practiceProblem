# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    l = list(s)
    print(any([ele.isalnum() for ele in l]))
    print(any([ele.isalpha() for ele in l]))
    print(any([ele.isdigit() for ele in l]))
    print(any([ele.islower() for ele in l]))
    print(any([ele.isupper() for ele in l]))




