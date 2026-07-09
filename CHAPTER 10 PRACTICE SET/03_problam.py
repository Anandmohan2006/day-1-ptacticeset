class  employee:
    salary = 10000
    increment = 1000
    
    @property
    def salaryAfterIncrement(self):
        return(self.salary + self.salary * (self.increment/100))
    
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100  
        
        
        
        
e = employee()
e.salaryAfterIncrement = 12345

print(e.increment)