'''
Created on 2016�?8�?15�?

@author: yuanyun.yy
'''
bingo = '小甲鱼是帅哥'
answer = input("请输入小甲鱼�?想听的一句话")
while True:
    if answer == bingo:
        break
    answer =input('抱歉，错了，请重新输入：')
print ('正确')

for i in range(10):
    if i%2 != 0:
        print(i) 
        continue   #条件符合跳出循环
    i +=2
    print(i)
    