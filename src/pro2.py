'''
Created on 2016年8月15日

@author: yuanyun.yy
'''
for i in range(10):
    if i%2 != 0:
        print(i) 
        continue   #条件符合跳出循环
    i +=2
    print(i)
    