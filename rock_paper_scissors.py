import random
import time

def end_game_stats(u,c,t,d):
    print(d +
          "\n              Thanks for playing! "
          "\n          You won a total of " + str(u) + " games"
          "\n          And the computer won " + str(c) + " games."
          "\n          There was a total of " + str(t) + " ties\n" + d)

dashes = "-----------------------------------------------------------------------"
i = 0

moves = ["Rock","Paper","Scissors"]
input_moves = {"r":"Rock", "p":"Paper", "s":"Scissors"}

uw = 0
cw = 0
ties = 0

print(dashes + "\n    Hi there my name is Will and I would like to play a game with you.")
time.sleep(1.5)
print( "\n          I would like to play Rock, Paper, Scissors with you \n                 Lets see who can win the most games?\n" + dashes)
# Intro text for the game.


while i == 0:
    computers_move = moves[(random.randint(0,2))]
    #print(computers_move) #For testing delete after
    user_input = input("Pleas enter in your move (r/p/s): ")

    #Checks to see if the users move is valid (i.e. either r/p/s) and if it is save it as their guess
    if user_input != "r" and user_input != "p" and user_input != "s":
        print("This is an invalid guess. Please enter in a valid move.")
    else:
        user_move = input_moves[user_input]

    # If it is a tie
    if user_move == computers_move:
        print("This is a tie.")
        ties += 1
        if input("Would you like to play again? (y/n)") == "y":
            print(dashes)
        else:
            end_game_stats(uw,cw,ties,dashes)
            i += 1

    #User chooses rock
    elif user_move == "Rock":
        if computers_move == "Scissors":
            print("The computer chose scissors. Well done you won!")
            uw += 1
            if input("Would you like to play again? (y/n)") == "y":
                print(dashes)
            else:
                end_game_stats(uw, cw, ties, dashes)
                i += 1
        else:
            print("Unlucky, the computer chose paper. You lose.")
            cw += 1
            if input("Would you like to play again? (y/n)") == "y":
                print(dashes)
            else:
                end_game_stats(uw, cw, ties, dashes)
                i += 1

    #User chooses paper
    elif user_move == "Paper":
        if computers_move == "Rock":
            print("The computer chose rock. Well done you won!")
            uw += 1
            if input("Would you like to play again? (y/n)") == "y":
                print(dashes)
            else:
                end_game_stats(uw, cw, ties, dashes)
                i += 1
        else:
            print("Unlucky, the computer chose scissors. You lose.")
            cw += 1
            if input("Would you like to play again? (y/n)") == "y":
                print(dashes)
            else:
                end_game_stats(uw, cw, ties, dashes)
                i += 1

    #User chooses scissors
    else:
        if computers_move == "Paper":
            print("The computer chose paper. Well done you won!")
            uw += 1
            if input("Would you like to play again? (y/n)") == "y":
                print(dashes)
            else:
                end_game_stats(uw, cw, ties, dashes)
                i += 1
        else:
            print("Unlucky, the computer chose rock. You lose.")
            cw += 1
            if input("Would you like to play again? (y/n)") == "y":
                print(dashes)
            else:
                end_game_stats(uw, cw, ties, dashes)
                i += 1

'''
Written by Jordan Kent

To do:
    - Bugs:
        - Fix invalid guesses restarting the game and not resulting in a match outcome

    - New features:
        - Feature to ask the user how many games they would like to play and then execute that many games
          and still display the game stats at the end of the time

'''