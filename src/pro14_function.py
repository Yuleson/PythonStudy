'''
Created on 2016年9月19日

@author: yuanyun.yy
'''
def myfirstfunction():
    print('我的第一个函数')
myfirstfunction() 
def mysecondfunction(name):    
    '带参数的函数'
    print(name+ "第二个函数")
mysecondfunction("我的")
def add(num1,num2):
    result = num1+num2
    print(result)
add(1,2)
def add1(num1,num2):            
    '带返回值的函数'
    return (num1+num2)
print(add1(2, 3))

