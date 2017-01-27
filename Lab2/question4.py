def is_good(n):
    return (n%7==0) and (n%5!=0) and n in range(2000,3200)

testList=list(range(0,10000))
goodList=(filter(is_good,testList))
for element in goodList:
    print(element,end=',')