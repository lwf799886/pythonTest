#coding=utf-8
print("你好,世界")

print ("hello");
print(" world");

if True:
    print("True")
else:
    print("false")

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)






numbers =[12,37,5,42,8,3]
even = []
odd =[]
while len(numbers)>0:
    number = numbers.pop()
    if(number %2 ==0):
        even.append(number)
    else:
        odd.append(number)

print(even);
print(odd)

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print("当前水果"+fruits[index])
print("goodbye")



import random


print(random.random())


import time
ticks =time.time()
print(ticks)

localstime = time.localtime(time.time())
print(localstime)

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

import calendar
cal = calendar.month(2016,1)
print(cal)


def printme( str ):
    print(str)
    return



print(printme("sada"))


#encoding=utf-8
fo=open("text","r+")
fo.read(10)
print(fo)





