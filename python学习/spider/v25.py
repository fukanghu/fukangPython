'''
search练习
'''

import re

s = r'\d+'

parttern = re.compile(s)

m = parttern.search("one12two34three56")
print(m.group())

# 参数表明搜查的起始范围
m = parttern.search("one12two34three56", 10, 40)
print(m.group())