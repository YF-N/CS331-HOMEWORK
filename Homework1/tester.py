#tester class hold necessary info of a tester

class tester():
    def __init__(self):
        print("Welcome to the test!\n")
        first=input("Please enter your first name >>>  ")
        last=input("Please enter your last name >>>  ")
        id=input("Please enter your ID >>>  ")

        self.fName=first
        self.lName=last
        self.ID=id

        self.testLog=[]
        self.answeredLog=[]

        self._score=0

    def info(self):
        return 'Tester name is: {} {}  Tester ID is: {}'.format(self.fName,self.lName,self.ID)

    def hello(self):
        print('>>> Hello {} {} (ID={}), your test is start! \n'.format(self.fName,self.lName,self.ID))

    def addLog(self,res=True,index=0):
        if res==True:
            self.testLog.append('{}:√'.format(index))
            self._score+=1
        else:
            self.testLog.append('{}:¢'.format(index))
        self.answeredLog.append(index)
        return res

    def isAnswered(self,index=0):
        if index in self.answeredLog:
            return True
        else:
            return  False

    def getScore(self):
        return self._score

    def recordLog(self):
        testHistory=open('testHistory.txt','a')
        log=str(self.testLog)
        testHistory.write('{0:10}|{1:15}|{2:15}|{3:70}|{4:5}\n'.format(self.ID,self.fName,self.lName,log,self._score))
        testHistory.close()
        return True

    def goodbye(self):
        print("Thank you, test is finished. Your score is:{}/10".format(self._score))

# Author: Yunfan Niu
# yniu3@hawk.iit.edu
# Illinois Institute of Technology
# Jan 20, 2017
