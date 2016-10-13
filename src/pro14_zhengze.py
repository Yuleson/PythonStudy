'''
Created on 2016年10月11日

@author: Administrator
'''
import re
string = r'he.llo'
pattern = re.compile(string)
string1 = 'hello,world!'
match = pattern.match(string1)
if match:
    print(string1)
else:
    print('没匹配项')