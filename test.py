import random
import time

target = random.randint(1,20)

i = 1
guess = 0
pb = 0

print("---------------------------------------------------------------------------\n    Hi there my name is Will and I would like to play a game with you.")
time.sleep(1.5)
print("\nIn this game I will pick a number from 1 - 20 and you will have to guess \nthe number. Each guess I will tell you whether you are higher or lower\n---------------------------------------------------------------------------\n")


def update_pb(n):
    new_pb = n
    return new_pb

while i != 0:
    user_guess = int(input("What is your guess: "))

    if user_guess == target:
        print("\nYou have guessed correctly")
        guess += 1
        print("It took you " + str(guess) + " guesses to get the target number.")
        if input("\nWould you like to play again (y/n): ") == "y":
            print("\n--------------------------------------\n")
            if guess != 0 or guess < pb:
                pb = update_pb(guess)
            guess = 0
            target = random.randint(1,20)
        else:
            if guess != 0 or guess < pb:
                pb = update_pb(guess)
            print("-------------------------------------------------"
                  "\n              Thanks for playing.              \nYour personal best this session was " + str(pb) + " guesses."
                  "\n-------------------------------------------------")
            i -= i
    elif user_guess > target:
        print("Your guess is higher than the target. Try again\n")
        guess += 1
    else:
        print("Your guess is lower than the target. Try again\n")
        guess += 1