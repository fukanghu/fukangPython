'''
findall案例
'''

import re
pattern = re.compile(r'\d+')

s = pattern.findall("i am 18 years old and 184 height")

print(s)

s = pattern.finditer("i am 18 years old and 184 height")

print(type(s))

for i in s:
    print(i.group())

