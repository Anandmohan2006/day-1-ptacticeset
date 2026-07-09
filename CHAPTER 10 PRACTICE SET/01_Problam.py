class twoDVector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    
    def show(self):
        print(f"the 2D vector is {self.x}i + {self.y}j")
        
        
    
    
class threeDvector(twoDVector):
    def __init__(self,x,y,z):
        super().__init__(x , y)
        self.z = z
    
    
    def show(self):
        print(f"the 2D vector is {self.x}i + {self.y}j + {self.z}z")
        
        
a = twoDVector(10,20)
a.show()

b = threeDvector(10,20,30)   
b.show() 

            