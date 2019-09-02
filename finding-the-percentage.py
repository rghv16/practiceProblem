# https://www.hackerrank.com/challenges/finding-the-percentage/problem


if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name, math, physics, chemistry = input().split(' ')
        total = float(math) + float(chemistry) + float(physics)
        total /= 3
        l.append((name, math, physics, chemistry, total))
    name = input()
    for ele in l:
        if ele[0] == name:
            print(f"{ele[4]:.2f}")

