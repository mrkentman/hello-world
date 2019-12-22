import random
import time

target = random.randint(1, 20)
print(target)  # REMOVE AFTER TESTING
i = 1
guess = 0
pb = 0

print(
    "---------------------------------------------------------------------------\n    Hi there my name is Will and I would like to play a game with you.")
time.sleep(1.5)
print(
    "\nIn this game I will pick a number from 1 - 20 and you will have to guess \nthe number. Each guess I will tell you whether you are higher or lower\n---------------------------------------------------------------------------\n")
# Intro text for the game.

while i != 0:
    user_guess = int(input(
        "What is your guess: "))  # Get the user guess. User guess can either be invalid, correct, above, or below. If expressions to determine what their guess is in relation the the target

    if user_guess > 20 or user_guess < 1:  # invalid guess
        print("This is not a vald guess. Please guess a number between 1 and 20.\n")
        # In case the user makes an invalid guess (i.e. the guess is not between 1 and 20) so that
        # they can repeat their guess without having it being added to their total.'''
    elif user_guess == target:  # correct guess
        print("\nYou have guessed correctly")
        guess += 1
        print("It took you " + str(
            guess) + " guesses to get the target number.")  # Increae guesses by 1 and informs player how many guesses it took them to win.

        if input("\nWould you like to play again (y/n): ") == "y":  # ask the player if they would like to try again
            print("\n--------------------------------------\n")
            if pb == 0 or guess < pb:  # updates the players pb if this is their first go (i.e their pb is 0 as they haven't done a game yet) or if that game was lower than the previous pb
                pb = guess
            guess = 0
            target = random.randint(1, 20)
            print(target)  # REMOVE AFTER TESTING
        else:
            if pb == 0 or guess < pb:  # updates the players pb if this is their first go (i.e their pb is 0 as they haven't done a game yet) or if that game was lower than the previous pb
                pb = guess
        print("-------------------------------------------------"
              "\n              Thanks for playing.              \nYour personal best this session was " + str(pb) + " guesses."
              "\n-------------------------------------------------")
        i -= 1  # ends the loop therefore ending the program/game
    elif user_guess > target:  # guess higher than the target
        print("Your guess is higher than the target. Try again\n")
        guess += 1
    else:  # if none of the other options are correct, then the guess is too low
        print("Your guess is lower than the target. Try again\n")
        guess += 1

'''To do:
    - Add way for when a '1' is displayed in the guesses it will say the singular version of guess
    and not the plural form.
        - This may be kind of hard as the guess variable is said within a string so
    - If a non-nummerical character is submitted for a guess have it return as an incorrect guess and not break the code
    - Remove the printing target commands that are being used for testing'''