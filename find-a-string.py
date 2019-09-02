# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    cnt = 0 
    l = len(sub_string)
    for i in range(0, len(string)-len(sub_string)+1 ):
        k = i
        for j in range(0, len(sub_string)):
            if sub_string[j] == string[k] :
                k += 1
                continue
            else:
                break
        if i + l == k:
            cnt += 1
        
    return cnt



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
