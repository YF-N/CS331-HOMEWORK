class tester(object):
    def __init__(self):
        print("Welcome to the test!\n")
        first=input("Please enter your first name >>>  ")
        last=input("Please enter your last name >>>  ")
        id=input("Please enter your ID >>>  ")

        self.fName=first
        self.lName=last
        self.ID=id

    def info(self):
        return 'Tester name is: {} {}  Tester ID is: {}'.format(self.fName,self.lName,self.ID)





