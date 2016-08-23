'''
Created on 2016å¹?8æœ?17æ—?

@author: yuanyun.yy
'''
list1 = [123]
list2 = [456]
print(list1>list2)
list3 = [123,456]
list4 = [234,123,456]
list5 = [123,456]
print((list3 < list4) and (list3 == list5) and (list4 > list5))
print(list3 + list4)
list6 =[123,234,[123,456],123,234]
print(list6[2][1])
print(456 in list6[2])
print(456 in list6)
print(list6.count(123))
print(list6.index(123,2,4))
list6.reverse()
print(list6)
list6.reverse()
list4.sort()
print(list4)
list4.sort(reverse = True)
list7 = list1
list8 = list1[:]
list1.append(234)
print(list1)
print(list7)
print(list8)

 


