# linear search

def linearSearch(alist, item):
    position = 0
    while position < len(alist):
        if alist[position] == item:
            return position
        position = position + 1
    return -1

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return -1

def fillList(b):
    i = 0
    while i != len(b):
        b[i] = i
        i = i + 1

import time

def testsearches(m=100):


    b = [0] * 1000000  # List to search

    fillList(b)
    print('list has been filled >>>',end=' ')
    for i in range(0,10):
        print(str(b[i]),end=' ')
    print("...")
    print ('\n\nRunning linear search ' + str(m) + ' times')

    start = time.time()

    i = 0

    while i < m:
        answer = linearSearch(b, len(b))
        i = i + 1
    end = time.time()
    diff = int(round((end - start) * 1000))

    print ('Time for linear search: ' + str(diff) + ' ms')

    print ('Running binary search ' + str(m) + ' times')

    fillList(b)

    start = time.time()
    i = 0

    while i < m:
        answer = binarySearch(b, len(b))
        i = i + 1
    end = time.time()
    diff = int(round((end - start) * 1000))

    print ('Time for binary search: ' + str(diff) + ' ms')

testsearches(100)