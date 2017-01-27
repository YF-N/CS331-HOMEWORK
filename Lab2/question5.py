def bull (target=[],guess=[]):
    targetSet=set(target)
    counter=0
    for letter in guess:
        if letter in targetSet:
            counter+=1
    return counter

def cow(target=[],guess=[]):
    index=0
    counter=0
    for letter in guess:
        if target[index]==letter:
            counter+=1
        index+=1
    return counter

from random import randint
answer=randint(1000,9999)
answerStr=str(answer)
#print(answerStr)
guessed=False
guessTime=0
while not guessed:
    guessTime+=1
    user=input("enter your number(4 digit) >>>")
    bulls=bull(answerStr,user)
    cows=cow(answerStr,user)
    if cows == 4:
        print ("you got it, you used {} times".format(guessTime))
        guessed = True
    else:
        print("cows: {}   bulls:  {}".format(cows,bulls))

