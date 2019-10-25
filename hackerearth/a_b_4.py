
while True:
    try:
        a = input().split()
        print(sum(map(int, a)))
    except Exception as e:
        break
