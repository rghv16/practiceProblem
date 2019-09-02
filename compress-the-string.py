[200~# Enter your code here. Read input from STDIN. Print output to STDOUT
        ## https://www.hackerrank.com/challenges/compress-the-string/problem
        import itertools
        s = input()
        for ele in itertools.groupby(s):
            print( (len(tuple(ele[1])), int(ele[0])),end=' ')

