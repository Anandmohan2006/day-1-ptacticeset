class calculator:
    
    def __init__(self, n):
        self.n = n
        
        
    def square(self):
        print(f"the square of {self.n*self.n}")
        
    def cube(self):
        print(f"the cube of {self.n*self.n*self.n}")
        
    def squaroot(self):
        print(f"the squaroot of {self.n**1/2}")  
        
    @staticmethod
    def hello():
        print("hello bacchoo" "\n")   
            
            
            
c = calculator(5)


c.hello()
c.square()
c.cube()
c.squaroot()