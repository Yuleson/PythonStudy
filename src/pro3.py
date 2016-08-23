'''


@author: yuanyun.yy
'''
num1 = int(input("请输入一个数ad"))
oper1 = input("请输入操作符")
num2 = int(input("请输入第二个数字"))
           
if oper1 == "+":
    print (num1+num2)
elif  oper1  == '-':
    print (num1-num2)
elif  oper1  == '*':
    print (num1*num2)
else:
    print (num1/num2)
