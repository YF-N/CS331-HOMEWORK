#question class hold necessary info of one single question

class question(object):
    def __init__(self,str=''):
        self.Qindex=str.find('#Q:')+3
        self.Oindex=str.find('#O:')+3
        self.Aindex=str.find('#A:')+3

        self.question=str[self.Qindex:self.Oindex-3]
        self.options = str[self.Oindex:self.Aindex - 3]
        self.answer = str[self.Aindex:]



    def getQuestion(self):
        return self.question

    def getOptions(self):
        return self.options

    def getAnswer(self):
        return self.answer


    def isCorrect(self,ans='No Answer'):
        if (self.answer.find(ans)>=0):
            print('\n>>> Your answer is CORRECT!\n')
            return True
        else:
            print('\n>>> Your answer is INCORRECT!   The CORRECT ANSWER is: {}\n'.format(self.answer))
            return False

    def ask(self):
        print('->Question: {}'.format(self.question))
        print('->Possible answers: {}\n'.format(self.options))
        answer=input('Please enter your answer (The whole word) >>>  ')
        if self.isCorrect(answer):
            return True
        else:
            return False

# Author: Yunfan Niu
# yniu3@hawk.iit.edu
# Illinois Institute of Technology
# Jan 20, 2017