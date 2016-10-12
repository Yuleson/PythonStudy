'''


@author: yuanyun.yy
'''
testarray = ['1','2','3','4','5']
print (testarray)
testarray.append('6')
print (testarray)
testarray.extend(['7','8'])
print (testarray)
testarray.insert(0, '0')
print (testarray)
print (len(testarray))
testarray.remove('0')
print (testarray)
del testarray[0]
print (testarray)
lastnum = testarray.pop()
print(lastnum)
print (testarray)
print(testarray[1:3],testarray[1:],testarray[:3],testarray[:])
mixarray = ['1','shuju',[1,2,3]]
print (mixarray)
emptyarray = []
print (emptyarray)
