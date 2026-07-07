
#program to get the (price, status, and trainNo) of a train that goes to new delhi to ballia


from random import randint

class train:
    
    def __init__(self , trainNo):
        self.trainNo =trainNo
        
    def book(self, fromm, to):
        print(f"ticket is conform in train no {self.trainNo} from {fromm} to {to}")
        
        
    def getstatus(self):
        print(f"train no : {self.trainNo} is running on time")
        
        
    def getfare(self, fromm , to):
        print(f"ticket fare in  train no {self.trainNo} from {fromm} to {to} is {randint(300,2000)}")
        
        
t = train(12345)
t.book("ballia" , "new delhi")
t.getstatus()
t.getfare("ballia" , "new delhi")