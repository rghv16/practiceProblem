# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(string):
    # your code goes here
    no_consonant = 0
    no_vowel = 0
    kst = 0
    sst = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            kst += len(string) - i
            continue
        sst += len(string) - i
    if kst>sst:
        print("Kevin", kst)
    elif kst < sst:
        print("Stuart",sst)
    else:
        print("Draw")
        
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
