class programer:
    company = "microsoft"
    
    def __init__(self, name , salary, address):
        self.name = name
        self.salary = salary
        self.address = address
        
        
p = programer ("satyam",600000,"delhi")      

print(p.name , "\n",p.salary, "\n",p.address, "\n", p.company)  

print(" ")

a = programer ("aditya",1230000,"kishnupur")      

print(a.name , "\n",a.salary, "\n",a.address)  

print(" ")

p = programer ("pandey",500000,"gujrat")      

print(p.name , "\n",p.salary, "\n",p.address)  
        