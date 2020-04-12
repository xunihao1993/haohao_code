import re


for i in  range(4):
    print(i)

a='发发'

pattern = re.compile(r'^[0-9]*?$')

if pattern.search(a) :
    print('匹配到');
else:
    print('没有匹配到')
