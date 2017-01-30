# Experiment 1
# Author: Yunfan Niu
# Test the list index operation

import timeit
import random
ß
timeList=[]
sizeList=list(range(1000,1000000,10000))
for n in range(1000,1000000,10000):
    list=[]
    for i in range (0,n):
        list.append(random.randint(0,n))
    index=random.randint(0,n)
    timer=timeit.Timer("list[%d]" %(index-1), "from __main__ import list" )
    time=timer.timeit(number=1000)
    timeList.append(time)
    print(str(n),":    ",str(time))

import matplotlib.pyplot as plt

plt.plot(sizeList,timeList,'b-')
plt.show()