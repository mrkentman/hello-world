    import random
    import time

    target = random.randint(1,20)
    print(target)
    i = 1
    guess = 0
    pb = 0

    print("---------------------------------------------------------------------------\n    Hi there my name is Will and I would like to play a game with you.")
    time.sleep(1.5)
    print("\nIn this game I will pick a number from 1 - 20 and you will have to guess \nthe number. Each guess I will tell you whether you are higher or lower\n---------------------------------------------------------------------------\n")
    #Intro text for the game.

print("---------------------------------------------------------------------------\n    Hi there my name is Will and I would like to play a game with you.")
time.sleep(1.5)
print("\nIn this game I will pick a number from 1 - 20 and you will have to guess \nthe number. Each guess I will tell you whether you are higher or lower\n---------------------------------------------------------------------------\n")
        user_guess = int(input("What is your guess: ")) #Get the user guess. User guess can either be invalid, correct, above, or below. If expressions to determine what their guess is in relation the the target

            #In case the user makes an invalid guess (i.e. the guess is not between 1 and 20) so that

    '''To do:
        - Add way for when a '1' is displayed in the guesses it will say the singular version of guess
        and not the plural form. 
            - This may be kind of hard as the guess variable is said within a string so'''