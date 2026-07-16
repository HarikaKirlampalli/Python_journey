'''DAY-21
 Self Keyword
 -------------
>>self refers to current object..

class Test:
    def display(self):
        print(self)
te = Test()
print(te)
te.display()

 Constructor
 ------------
>>This constructor initializes the object automatically when it is created...

class Batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
B4 = Batch()
B4.display()

Access Specifier
------------------
class Batch:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self._name)
        print(self.branch)
B4 = Batch('Harika' , ' cSE')
B4.display()

@2
class fam:
    def __init__(self):
        self._name = "Harika"
f = fam()
print(f._name)

@3
class bank:
    def __init__(self):
        self.__pin = '2315'

AC= bank()
print(AC._bank__pin)#private varaiable outside the class
@4
class bank:
    def __init__(self):
        self.__pin = '2315'
    def display(self):
        print(self.__pin)
ac= bank()
ac.display()

Encapsulation
--------------
>>Means wrapping the data and methods into a single unit(class) while controlling access to the data..

'''
class atm:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,amount):
        self._balance += amount
        print(self._balance)
tran = atm(balance = int(input("Enter Amount: ")))
tran.deposit(amount = int(input("Enter Amount:")))














