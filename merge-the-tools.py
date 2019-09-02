# https://www.hackerrank.com/challenges/merge-the-tools/problem
def merge_the_tools(string, k):
    l = []
    for i in range(len(string) // k):
        st = string[i*k:(i+1)*(k)]
        p = []
        for ele in st:
            if not ele in p:
                p.append(ele)
        print(''.join(p))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
