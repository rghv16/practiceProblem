# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
import string
st = string.ascii_lowercase + string.ascii_uppercase +string.digits

def fun(s):
    # return True if s is a valid email, else return False
    is_extension = (3 >= len(s[s.find('.')+1:]))
    is_valid_username = all( ele in st+'-_' for ele in s[:s.find('@')]) and     len(s[:s.find('@')]) > 0
    is_valid_extension = all(ele in st for ele in s[s.find('@')+1:s.find('.')])
    return is_extension and is_valid_extension and is_valid_username

def filter_mail(emails):
