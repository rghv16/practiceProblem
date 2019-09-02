# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser
# https://www.hackerrank.com/challenges/html-parser-part-1/problem


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for att in attrs:
            print('->',att[0],'>',att[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for att in attrs:
            print('->',att[0],'>',att[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

