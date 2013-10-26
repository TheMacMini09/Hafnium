from os import system
from sys import exit
from time import sleep

wait = sleep
#cont is the variable used when continuing to the next page or the start
cont = ""
userSelection = 0
operSys = ""
clearScreen = ''

operSys = input("Are you on (M)ac/Unix or (W)indows?")

if operSys == "M":
    clearScreen = 'clear'
elif operSys == "W":
    clearScreen = 'cls'

while True:
    system(clearScreen)
    print("Welcome to Michael Barker's program for info on the element Hafnium!")
    print("To begin, type the number of one of the following options to see information:")
    print(" (1) General Information (Atomic weight, etc.)")
    print(" (2) Discovery of Hafnium")
    print(" (3) Properties of Hafnium")
    print(" (4) Uses of Hafnium")
    print(" (5) Processing of Hafnium")
    print(" (6) Hafnium's safety hazards and necessary precautions")
    print(" (7) Compounds that include Hafnium")
    print(" (8) Sources used")
    print(" (9) Quit the program")
    
    userSelection = int(input("#"))
    system(clearScreen)
    if userSelection == 1:
        print("This is the contents of selection 1.")
        cont = input("Press Enter to return to the main menu...")
        break
    elif userSelection == 2:
        print("This is the contents of selection 2.")
        break
    elif userSelection == 3:
        print("This is the contents of selection 3.")
        break
    elif userSelection == 4:
        print("This is the contents of selection 4.")
        break
    elif userSelection == 5:
        print("This is the contents of selection 5.")
        break
    elif userSelection == 6:
        print("This is the contents of selection 6.")
        break
    elif userSelection == 7:
        print("This is the contents of selection 7.")
        break
    elif userSelection == 8:
        print("This is the contents of selection 8.")
    elif userSelection == 9:
        print("Good-bye!")
        system(clearScreen)
        quit()
        
print("Hello")
