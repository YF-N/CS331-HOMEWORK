# Experiment 2
# Author: Yunfan Niu
# Test the dict get and set operation

import timeit
import random

listDelTime=[]
dictDelTime=[]
sizeList=list(range(5000,1000000,10000))
for n in range(5000,1000000,10000):
    dict={}
    list = []
    for i in range(0, n):
        list.append(random.randint(0, n))
    for i in range (0,n):
        randomValue=random.randint(0,n)
        dict[i]=randomValue

    index=random.randint(0,n-2)
    timerDict=timeit.Timer("if %d in dict: del dict[%d]" %(index,index), "from __main__ import dict,index" )
    timerList=timeit.Timer("del list[%d]" %(1), "from __main__ import list,index" )
    timeList=timerList.timeit(number=1000)
    timeDict=timerDict.timeit(number=1000)

    listDelTime.append(timeList)
    dictDelTime.append(timeDict)
    print(str(n),":    list:",str(timeList),"    dict:",str(timeDict),"   ",str(len(list)))

import matplotlib.pyplot as plt

plt.plot(sizeList,listDelTime,'b-',sizeList,dictDelTime,'r-')
#plt.ylim(0,0.001)
plt.xlabel("Size of the dict&list")
plt.ylabel("Time of del execution")
plt.title("Test of dict(O(1))(red) and list(O(n))(blue) del operation ")
plt.show()