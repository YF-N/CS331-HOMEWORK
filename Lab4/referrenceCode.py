# linear search algorithm

def linearSearch(alist, item):
    position = 0
    found = False
    while position < len(alist) and not found:
        if alist[position] == item:
            found = True
        position = position + 1
    return found


# binary search algorithm

def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# this function inserts sorted data into a list

def fill_pos(b):
    """Fill list b: put i in b[i]."""
    # inv: have filled in b[0..i-1]
    i = 0
    while i != len(b):
        b[i] = i
        i = i + 1


# You need to import time module

import time

# this function compares running time of linear and binary search algorithms.
#Here m is number of time you want to search using each algorithm.Each time they search last element of the list.


def testsearches(m=100):
    # Execute linear search and binary search m times on a list of #100000 elements. Print results
    # Precondition: m >= 0."""

    b = [0] * 1000000  # List to search

    print ('Populating sorted list')
    fill_pos(b)

    # Run linear search m times and print the results
    print ('Running linear search ' + str(m) + ' times')

    timestart = time.time()
    # inv: have done iterations 0..i-1
    i = 0
    # inv: linear_search has been called i times.
    while i < m:
        answer = linearSearch(b, len(b))
        i = i + 1
    timeend = time.time()
    diff = int(round((timeend - timestart) * 1000))

    print ('Time for linear search: ' + str(diff) + ' ms')

    # Run binary search m times and print the results
    print ('Running binary search ' + str(m) + ' times')

    fill_pos(b)

    timestart = time.time()
    # inv: have done iterations 0..i-1
    i = 0
    # inv: binary_search has been called i times.
    while i < m:
        answer = binarySearch(b, len(b))
        i = i + 1
    timeend = time.time()
    diff = int(round((timeend - timestart) * 1000))

    print ('Time for binary search: ' + str(diff) + ' ms')