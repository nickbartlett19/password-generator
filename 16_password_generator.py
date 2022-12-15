#  ____                                     _ 
# |  _ \ __ _ ___ _____      _____  _ __ __| |
# | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
# |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
# |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
#                                        
#   ____                           _             
#  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
# | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
#  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
#
# password_generator.py is a program that generates passwords based on user
# specifications like length, types of characters, and upper/lower case. It has the 
# additional features of storing a log of previoius passwords, and being able to save
# them to a text file.

import random 
import string
import datetime

# Command Functions

def Command():  

    # Show user available commands
    print("------------")
    print("Available Commands:")
    print("0: Program Information.")
    print("1: Change Password Specifications.")
    print("2: Generate Password.")
    print("3: Show previous passwords.")
    print("4: Store previous passwords to .txt file.")
    print("5: Exit Program.")
    print("------------")

    status = True
    while status == True:
        command = input("Enter Command: ")
        if command.isnumeric() == True and int(command) in range(0,6):
            command = int(command)
            break
        elif command.isnumeric() == False or int(command) not in range(0,6):
            print(f"Your command, {command} is not a number between 0 and 5. ")
        else:
            print("Something went wrong in Command(). Exiting ... ")

    if command == 0:
        GiveInformation()
    elif command == 1:
        ChangeSpecifications()
    elif command == 2:
        print(GeneratePassword())
    elif command == 3:
        PasswordLog()
    elif command == 4:
        StorePasswords()
    elif command == 5:
        Exit()

def GiveInformation():
    print("Command 0: Program Information.")
    with open("/Users/nickbartlett/Code/Python/practicepython.org/16_password_generator/program_information.txt") as program_information:
        print(program_information.read())

def ChangeSpecifications():
    print("Command 1: Change Specifications.")
    print("0: Change Password Length.")
    print("1: Allow Uppercase Letters.")
    print("2: Allow Numbers.")
    print("3: Allow Special Characters (e.g. !%$#)")

    status = True
    while status == True:
        command = input("Enter Command: ")
        if command.isnumeric() == True and int(command) in range(0,4):
            command = int(command)
            break
        elif command.isnumeric() == False or int(command) not in range(0,4):
            print(f"Your command, {command} is not a number between 0 and 3. ")
        else:
            print("Something went wrong in ChangeSpecifications(). Exiting ... ")
            exit()
    
    if command == 0:
        PasswordLength()
    elif command == 1:
        PasswordCase()
    elif command == 2:
        PasswordNumbers()
    elif command == 3:
        PasswordSpecial()
    else:
        print("Something went wrong in ChangeSpecifications(). Exiting ... ")
        exit()

# ChangeSpecifications() subfunctions

def PasswordLength():

    status = True
    while status == True:
        input_length = input("Please enter desired length (1-16): ")
        if input_length.isnumeric() == True and int(input_length) in range(1,17):
            break
        elif input_length.isnumeric() == False or int(input_length) not in range(1,17):
            print("Desired length is not an integer between 1 and 16 ")
        else:
            print("Something went wrong with PasswordLength. Exiting ... ")
            exit()
    
    spec[0] = int(input_length)
    print(f"Password length changed to {input_length} characters.")

def PasswordCase():

    status = True
    while status == True:
        case = input("To allow uppercase characters, type 1, otherwise, type 0: ")
        if case.isnumeric() == True and int(case) in range(0,2):
            break
        elif case.isnumeric() == False or int(case) not in range(0,2):
            print("Command is not 1 or 0.")
        else:
            print("Something went wrong with PasswordCase. Exiting ... ")
            exit()
    if int(case) == 1:
        spec[1] = True
        print("Uppercase characters will be used.")
    elif int(case) == 0:
        spec[1] = False
        print("Uppercase characters will not be used.")
    else: 
        print("Something went wrong with PasswordCase. Exiting ... ")
        exit()

def PasswordNumbers():
    status = True
    while status == True:
        case = input("To allow numerical characters, type 1, otherwise, type 0: ")
        if case.isnumeric() == True and int(case) in range(0,2):
            break
        elif case.isnumeric() == False or int(case) not in range(0,2):
            print("Command is not 1 or 0.")
        else:
            print("Something went wrong with PasswordNumbers. Exiting ... ")
            exit()
    if int(case) == 1:
        spec[2] = True
        print("Numerical characters will be used.")
    elif int(case) == 0:
        spec[2] = False
        print("Numerical characters will not be used.")
    else: 
        print("Something went wrong with PasswordNumbers. Exiting ... ")
        exit()

def PasswordSpecial():
    status = True
    while status == True:
        case = input("To allow special characters, type 1, otherwise, type 0: ")
        if case.isnumeric() == True and int(case) in range(0,2):
            break
        elif case.isnumeric() == False or int(case) not in range(0,2):
            print("Command is not 1 or 0.")
        else:
            print("Something went wrong with PasswordSpecial(). Exiting ... ")
            exit()
    if int(case) == 1:
        spec[3] = True
        print("Special characters will be used.")
    elif int(case) == 0:
        spec[3] = False
        print("Special characters will not be used.")
    else: 
        print("Something went wrong with PasswordSpecial(). Exiting ... ")
        exit()

# More Command Functions

def PasswordLog():
    print("Command 3: Password Log.")
    
    for i in range(0, len(log)):
        print(f"{i}: {log[i]}")

def StorePasswords():
    with open('saved_passwords.txt', 'a') as f:
        f.write("------------\n")
        f.write(str(datetime.datetime.now()) + "\n")
        f.write("Password Log.\n")
        for password in log:    
            f.write(password + "\n")
        f.write("------------\n")

def Exit():
    print("Exiting ... ")
    exit()

# GeneratePassword() Function

def GeneratePassword():
    print("Generating Password ...")
    password = ""

    # lowercase letters always allowed
    possible_characters = lowercase_letters

    # allow uppercase, if specified
    if spec[1] == True:
        possible_characters = possible_characters + uppercase_letters
    
    # allow numbers, if specified
    if spec[2] == True: 
        possible_characters = possible_characters + numbers

    # allow special chars, if specified
    if spec[3] == True:
        possible_characters = possible_characters + special_characters

    # choose password chars one by one
    for i in range(0, spec[0]):
        password = password + random.choice(possible_characters)

    # Add new password to log for PasswordLog()
    log.append(password)

    return password

# Main()

# make lists of characters by type
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
numbers = [str(x) for x in range(0,10)]
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# Make default password specifications and empty log list
# format is spec = [Length (int in 0-16), UpperCase, Numbers, SpecialCharacters]
log = []
spec = [8, True, True, False]

print("A Password Generator by Nick Bartlett")
print("Specifications set to default.")

# Keep looping until keyboard interrupt or user uses exit command

status = True
while status == True:
    Command()
