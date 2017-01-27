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
print(descending_bubble(testList))
