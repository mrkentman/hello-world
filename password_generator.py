import random
import time

def loading():
    for x in range(0,3):
        time.sleep(1)
        print("*")

one_to_32 = list(range(1,33))

alpha_and_nums = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1','2','3','4','5','6','7','8','9','0')
symbols = ('!','£','$','%','^','&','*','(',')','-','_','=','+','@','#','~','/','?')

i = 0
j = 0
dashes = "---------------------------------------------------------------------"
password = ""

while i == 0:
    user_input_length = int(input("How long do you want the password to be? (Max character length is 32) "))
    if user_input_length in one_to_32:
        i += 1
        while j == 0:
            user_character = input("Do you want to include special characters in the password? (y/n)")
            if user_character == "y":
                #line to remove all the special charcters from the list of available characters
                j += 1
            elif user_character == "n":
                j += 1
            else:
                print("Pleas enter either \"y\" for yes, \"n\" for no for if you would like to include special characte"
                      "rs in your password.\n")
    else:
        print(dashes + "\nThe password length you have entered is not valid. Please enter a\nnumber between 1 - 32 of "
                        "how long you would like your password to be.\n" + dashes)

if user_character == "y":
    chara_lib = alpha_and_nums + symbols
    lib_length = 80
else:
    chara_lib = alpha_and_nums
    lib_length = 62

for x in range(0,user_input_length):
   password += chara_lib[random.randint(0,lib_length-1)]

print("Generating password")
loading()
time.sleep(0.5)
print(dashes + "\nYour randomly generated password is: " + password + "\n" + dashes)

'''
Written by Jordan Kent

To do:
    -
'''