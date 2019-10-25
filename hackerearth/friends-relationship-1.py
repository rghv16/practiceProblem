#print(len("*################*"))

for _ in range(int(input())):
   # '^^^^^center^^^^^'
   #for align, text in zip('<^>', ['left', 'center', 'right']):
   #`{0:{fill}{align}16}'.format(text, fill=align, align=align)
   
   num = int(input())
   fill='*'
   width = num * 2
   
   for row in range(num-1, -1, -1):
       print('{0:{fill}^{width}}'.format(row*'##', fill=fill, width=width))
