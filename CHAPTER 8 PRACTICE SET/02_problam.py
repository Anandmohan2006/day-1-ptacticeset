import random

def game():
    print("You are playing the game...")
    return random.randint(1, 100)

score = game()

# Fetch high score
with open("highscore.txt") as f:
    highscore = f.read()

if (highscore != ""):
    highscore = int(highscore)
else:
    highscore = 0

print(f"Your score: {score}")

if score > highscore:
    with open("highscore.txt", "w") as f:
        f.write(str(score))
       
        
        
        
        


# from sys import set_coroutine_origin_tracking_depth
# import random
# from tkinter import scrolledtext


# def game():
#     print("you are playing the game...")
#     return random.randint(1 , 100)

# mistake ( score = game())
# #fetch the high score

# with open("highscore.txt") as f:
#     highscore = f.read()
#     if (highscore == ""):
#         highscore = int(highscore)
        
#     else:
#         highscore = 0

# print(f"your score {score}")
# if(score > highscore):
    
#     with open("highscore.txt" , "w") as f:
#       f.write(str(score))
      
      
# return score




# game ()



