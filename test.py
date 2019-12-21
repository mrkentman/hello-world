import random

target = random.randint(1,20)

i = 0
guess = 0
pb = guess

while i == 0:
    user_guess = int(input("What is your guess: "))

    if user_guess == target:
        print("\nYou have guessed correctly")
        guess += 1
        print("It took you " + str(guess) + " guesses to get the target number.")

        if input("\nWould you like to play again (y/n): ") == "y":
            guess = 0
            target = random.randint(1,20)
            print(target)

        else:
            print("\nThanks for playing.\nYour personal best this session was " + str(pb) + " guesses.")
            i += 1

    elif user_guess > target:
        print("Your guess is higher than the target. Try again\n")
        guess += 1
    else:
        print("Your guess is lower than the target. Try again\n")
        guess += 1
