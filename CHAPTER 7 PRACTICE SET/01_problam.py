# program for the gretest no taking by user using the fubction()



def greatest(a, b, c):

    if a > b and a > c:
        print("a is the greatest")

    elif b > a and b > c:
        print("b is the greatest")

    else:
        print("c is the greatest")


a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

greatest(a, b, c)