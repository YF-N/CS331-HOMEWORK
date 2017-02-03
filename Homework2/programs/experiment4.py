def combsort(unsort,pos):
    gap = len(unsort)
    swap = True
    while gap > 1 or swap:
        gap = max(1, int(gap / 1.25))  # gap always>1
        swap = False
        for i in range(len(unsort) - gap):
            j = i+gap
            if unsort[i] > unsort[j]:
                unsort[i], unsort[j] = unsort[j], unsort[i]
                swap = True
    return (unsort,unsort[pos-1])

list=[5,3,7,6,4,2,6,2,22345,453,8389,235,4,345,2345,23454,5,52453,45,23534,54,5,54245,3543,423]
print(list)
print(combsort(list,3))