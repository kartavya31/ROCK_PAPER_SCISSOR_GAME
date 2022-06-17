from pickle import FALSE
from random import randint
t = ["Rock","Paper","Scissor"] #creating a list of play options
computer = t[randint(0,2)] #assigning a random play to the computer
player = False  #set player to False
while player == False:
    player == input("Rock","Paper","Scissors") #set player to True
    if player == computer:
        print("Tie!!")
    elif player == "Rock":
        if computer == "Paper":
            print("You LOSE!!",computer,"covers",player)
        else:
            print("You WIN!!",player,"covers",computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You LOSE!!",computer,"covers",player)
        else:
            print("You WIN!!",player,"covers",computer)           
    elif player == "Paper":
        if computer == "Scissors":
            print("You LOSE!!",computer,"covers",player)
        else:
            print("You WIN!!",player,"covers",computer)           
    else:
        print("THIS IS NOT A VALID PLAY!!!!!") #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)] 
        