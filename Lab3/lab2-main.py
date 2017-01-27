# This is the lab3 of cs331
# Author: Yunfan Niu (Github: YF-N)
# yunfan.niu@outlook.com
# Illinois Institute of Technology
# Jan 26 2017

def descending_bubble(alist=[]):
    for sorted in range(len(alist)-1, 0, -1):
        for sorting in range(sorted):
            if alist[sorting] < alist[sorting + 1]:
                temp = alist[sorting]
                alist[sorting] = alist[sorting + 1]
                alist[sorting + 1] = temp
    return alist


testList = [33, 45, 67, 89, 23, 42, 62, 1, 85, 26]
#print(descending_bubble(testList))

def descending_insertion(alist=[]):
    for sorted in range(1,len(alist)):
        for sorting in range(sorted,0,-1):
            if alist[sorting]>alist[sorting-1]:        #current position is not good for the one is sorting
                temp = alist[sorting]
                alist[sorting] = alist[sorting - 1]
                alist[sorting - 1] = temp
            else:                                       #current position is good for the one is sorting
                break                                   #go to the next item of outer loop
    return alist


#print(descending_insertion(testList))
#function to generate a random list
import random
def randomList(size=1):
    list=[]
    for i in range(0,size):
        randnum=random.randint(0,size)
        list.append(randnum)
    return list

#creat a list to record all testing time in order to plot the result

br_l=[]
bw_l=[]
ir_l=[]
iw_l=[]
size_l=[]
# code below try to test the speed of both of sort function

import timeit
print('      size   ','      bubble_random    ','       bubble_worst    ',' insertion_random   ','    insertion_worst   ','unit=ms\n')
for size in range(1000,11001,100):
    #An ascending list is worst case for descending sort function

    bubble_random=timeit.Timer(
        "descending_bubble(randomList(%d))" %size,"from __main__ import descending_bubble,randomList" )
    bubble_worst=timeit.Timer(
        "descending_bubble(list(range(%d)))" %size,"from __main__ import descending_bubble" )
    insertion_random = timeit.Timer(
        "descending_insertion(randomList(%d))" % size, "from __main__ import descending_insertion,randomList")
    insertion_worst = timeit.Timer(
        "descending_insertion(list(range(%d)))" % size, "from __main__ import descending_insertion")

    br_t=bubble_random.timeit(number=1)
    bw_t=bubble_worst.timeit(number=1)
    ir_t=insertion_random.timeit(number=1)
    iw_t=insertion_worst.timeit(number=1)

    print("{0:10}   {1:20.3f}   {2:20.3f}   {3:20.3f}   {4:20.3f}".format(size,br_t,bw_t,ir_t,iw_t))

    size_l.append(size)
    br_l.append(br_t)
    bw_l.append(bw_t)
    ir_l.append(ir_t)
    iw_l.append(iw_t)

# code belowing try to plot the result

import numpy as np
import matplotlib.pyplot as plt

plt.plot(size_l,br_l,'r-',size_l,bw_l,'r--',size_l,ir_l,'b-',size_l,iw_l,'b--')
plt.xlabel('List size')
plt.ylabel('Sorting Time /ms')
plt.title('Bubble sorting (red) VS Insertion sorting(blue)\n worst case=dotted-line | random case=solid-line')
plt.show()