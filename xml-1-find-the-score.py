import sys
import xml.etree.ElementTree as etree


# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
def get_attr_number(node):
    # your code goes here
    total_score = len(node.attrib)
    for child in node:
        total_score +=  get_attr_number(child)
    return total_score


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
