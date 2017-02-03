# Experiment 2
# Author: Yunfan Niu
# Test the dict get and set operation

import timeit
import random

timeGetList=[]
timeSetList=[]
sizeList=list(range(5000,1000000,10000))
for n in range(5000,1000000,10000):
    dic={}
    for i in range (0,n):
        randomValue=random.randint(0,n)
        dic[n]=randomValue
    key=random.randint(0,n-1)
    timerGet=timeit.Timer("if %d in dic: dic[%d]" %(key,key), "from __main__ import dic" )
    timerSet=timeit.Timer("if %d in dic: dic[%d]=0" %(key,key), "from __main__ import dic" )
    timeGet=timerGet.timeit(number=1000)
    timeSet=timerSet.timeit(number=1000)

    timeGetList.append(timeGet)
    timeSetList.append(timeSet)
    print(str(n),":    get:",str(timeGet),"    set:",str(timeSet))

import matplotlib.pyplot as plt

plt.plot(sizeList,timeGetList,'b-',sizeList,timeSetList,'r-')
plt.ylim(0,0.001)
plt.xlabel("Size of the dict")
plt.ylabel("Time of execution")
plt.title("Test of dict set(red) and get(blue) operation ")
plt.show()