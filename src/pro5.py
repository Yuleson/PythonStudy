'''
Created on 2016�?8�?15�?

@author: yuanyun.yy
'''
score = int(input("请输入一个分�?"))
if score > 90:
    print ("A")
elif 80 <= score < 90:
    print ("B")
elif 60 <= score < 80:
    print ("C") 
elif 0 <= score <60: 
    print ("D")
else:
    print ("输入有误�?")