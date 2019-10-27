'''


'''


import re


if __name__ == '__main__':
    text = list()
    N = int(input())

    for _ in range(N):
        text.append(input())
    
    t = int(input())
    for _ in range(t):
        pattern = re.compile(r'\b'+input()+r'\b')  
        cnt = 0  
        for ele in text:
            cnt += len(pattern.findall(ele))
        print(cnt)
