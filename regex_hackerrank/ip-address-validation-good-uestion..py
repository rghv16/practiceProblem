import re

'''

ip address validation program
Question : detect valid ip[46] addresses, i have rearrange the building blocks for ipv4 

'''


PATTERN_IPV4 = r'^([0-9]|[0-9][0-9]|2[0-4][0-9]|25[0-5]|1[0-9][0-9])\.([0-9]|[0-9][0-9]|2[0-4][0-9]|25[0-5]|1[0-9][0-9])\.([0-9]|[0-9][0-9]|2[0-4][0-9]|25[0-5]|1[0-9][0-9])\.([0-9]|[0-9][0-9]|2[0-4][0-9]|25[0-5]|1[0-9][0-9])$'


PATTERN_IPV6 = r'^[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}:[0-9a-f]{1,4}$'

if __name__ == '__main__':
    for _ in range(int(input())):
        inp = input()
        if bool(re.search(PATTERN_IPV4, inp)):
            print('IPv4')
        elif bool(re.search(PATTERN_IPV6, inp)):
            print('IPv6')
        else:
            print('Neither')
        


