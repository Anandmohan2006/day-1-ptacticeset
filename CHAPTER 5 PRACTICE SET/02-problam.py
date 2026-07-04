marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2:"))
marks3 = int(input("Enter marks for subject 3: "))
marks4 = int(input("Enter marks for subject 4: "))
marks5 = int(input("Enter marks for subject 5: "))

#checking the percentage

percentage = (marks1 + marks2 + marks3 + marks4 +marks5)/500* 100


if (percentage >= 35 and marks1 >= 35 and marks2 >= 35 and marks3 >= 35 and marks4 >= 35 and marks5 >= 35):
    print("You have passed the exam :", percentage)

else:
    print("better luck next time :",percentage)

