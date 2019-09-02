from html.parser import HTMLParser

# https://www.hackerrank.com/challenges/html-parser-part-2/problem
class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)

    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data != '\n':
            print(data)
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


