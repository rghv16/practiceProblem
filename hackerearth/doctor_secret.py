len_name, num_page = map(int, input().split())

if len_name <= 23 and (500 < num_page <= 1000):
    print('Take Medicine')
else:
    print('Don\'t take Medicine')

