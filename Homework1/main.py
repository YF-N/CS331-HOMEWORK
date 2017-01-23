# This is the main source code for CS331-HW1
# Author: Yunfan Niu
# yniu3@hawk.iit.edu
# Illinois Institute of Technology

__Author__='Yunfan Niu'

from question import question
from tester import tester
from random import randint

questionPerTester=10

questionBank=open('questions.txt','r')
queCounter=0
ansCounter=0
questionList=[]

while queCounter<12:
    newQuestion=question(questionBank.readline())
    questionList.append(newQuestion)
    queCounter += 1

questionBank.close()
print("\n\nQuestions loading successfully...\n")

newTester=tester()
newTester.hello()

while ansCounter<questionPerTester:
    nextIndex=randint(0,11)
    if not newTester.isAnswered(nextIndex):
        correct=questionList[nextIndex].ask()
        if correct:
            newTester.addLog(True,nextIndex)
        else:
            newTester.addLog(False,nextIndex)

        ansCounter+=1

newTester.recordLog()
newTester.goodbye()




