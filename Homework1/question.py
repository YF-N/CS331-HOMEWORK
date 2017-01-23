class question(object):
    def __init__(self,str=''):
        self.Qindex=str.find('#Q:')+3
        self.Oindex=str.find('#O:')+3
        self.Aindex=str.find('#A:')+3

        self.question=str[self.Qindex:self.Oindex-3]
        self.options = str[self.Oindex:self.Aindex - 3]
        self.answer = str[self.Aindex:]

        self.index=str[:str.find(end='.')]

    def getQuestion(self):
        return self.question

    def getOptions(self):
        return self.options

    def getAnswer(self):
        return self.answer


    def isCorrect(self,ans='No Answer'):
        if (self.answer.find(ans)>=0):
            print('Your answer is correct!')
            return True
        else:
            print('Your answer is not correct!   The answer is: {}'.format(self.answer))
            return False
