#writting a program to perform  the factorial of given numbers using loops

n = int(input("Enter the  number:"))

multiply = 1

for i in range(1 , n+1):
    multiply = multiply *i
    
    
print(f"factorial of {n} is {multiply}")