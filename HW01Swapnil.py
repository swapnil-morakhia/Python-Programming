import random

moves =["rock","paper","scissor"]
cmove = None #this is a computer move
pmove = None #this is a player move

def game(cmove,pmove):
    #defining a method game
    while True:    
        # cmove chooses randomly from "moves" list
        cmove = random.choice(moves)
        #input from the user
        pmove = input ("What is your move? (choose from 'rock' 'paper' 'scissor' 'quit' 'exit'): ")
        #if elif else structure begins
        if cmove == pmove:
            print("The computer choose ",cmove)
            print ("Its a tie")
        elif pmove == "rock" and cmove == "scissor":
            print("The computer choose ",cmove)
            print ("Player wins")
        elif pmove == "rock" and cmove == "paper":
            print("The computer choose ",cmove) 
            print ("Computer wins")
        elif pmove == "paper" and cmove == "rock": 
            print("The computer choose ",cmove)
            print ("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            print("The computer choose ",cmove) 
            print ("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            print("The computer choose ",cmove) 
            print ("Player wins")
        elif pmove == "scissors" and cmove == "rock":
            print("The computer choose ",cmove) 
            print ("Computer wins")
        elif pmove == "paper" and cmove == "scissor":
            print("The computer choose ",cmove)
            print("Computer Wins")
        elif (pmove in ("exit", "quit")) and (cmove in ("rock", "paper" ,"scissor")):
            print ("goodbye! If you wish to play again you have to run the program")
            #if this condition, break
            break
        else:
            print("please enter a valid input: rock or paper or scissor or quit or exit : ")

#invoking method        
game(cmove,pmove)
