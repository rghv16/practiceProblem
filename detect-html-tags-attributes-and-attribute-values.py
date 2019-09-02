# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
from html.parser import HTMLParser

class Myparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for ele in attrs:
            print('->', ele[0],'>',ele[1])
    def handle_comment(self, data):
        return None
    
parser = Myparser()
for _ in range(int(input())):
    parser.feed(input())




