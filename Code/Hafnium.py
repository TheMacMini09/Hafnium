from os import system
from sys import exit
from time import sleep
import tkinter

wait = sleep
#cont is the variable used when continuing to the next page or the start
cont = ""
userSelection = 0
operSys = ""
clearScreen = ''

operSys = input("Are you on (M)ac/Unix or (W)indows?").lower()

if operSys == "m":
    clearScreen = 'clear'
elif operSys == "w":
    clearScreen = 'cls'

while True:
    system(clearScreen)
    print("Welcome to Michael Barker's program for info on the element Hafnium!")
    print("To begin, type the number of one of the following options, and press enter,")
    print("to see the information it contains:\n")
    print(" (1) General Information (Atomic weight, etc.)")
    print(" (2) Discovery of Hafnium")
    print(" (3) Properties of Hafnium")
    print(" (4) Uses of Hafnium")
    print(" (5) Processing of Hafnium")
    print(" (6) Hafnium's safety hazards and necessary precautions")
    print(" (7) Compounds that include Hafnium")
    print(" (8) Sources used")
    print(" (9) Quit the program")
    
    userSelection = int(input(" #"))
    system(clearScreen)
    if userSelection == 1:
        print("General Information of Halfnium (1,2)")
        print()
        print("{0:30s} Hafnium".format("Name:"))
        print("{0:30s} Hf".format("Symbol:"))
        print("{0:30s} 72".format("Atomic Number:"))
        print("{0:30s} 178.49".format("Atomic Weight:"))
        print("{0:30s} Solid".format("State at Room Temperature:"))
        print("{0:30s} 4".format("Group in Periodic Table:"))
        print("{0:30s} 6".format("Period in Periodic Table:"))
        print("{0:30s} Grey".format("Colour:"))
        print("{0:30s} Transition Metal".format("Element Category:"))
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen)
        break

    elif userSelection == 2:
        print("Discovery of Hafnium (1, 3)")
        print("Halfnium was discovered in 1923 by Dirk Coster and George Charles von Hevesy")
        print("in Copenhagen, Denmark. Halfnium comes from the latin name Hafnia, meaning")
        print("Copenhagen. To discover the 72nd elemt, Coster and von Hevesy analyzed ores")
        print("such as zirconium with x-ray spectography. Halfnium can be isolated into a ")
        print("pure form from Hafnium Tetraiodide (HfI4). The HfI4 is decomposed on a tungsten")
        print("filament, which makes a crystal bar of Hafnium. This is called the crystal")
        print("bar process.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen)
        break

    elif userSelection == 3:
        print("Properties of Hafnium")
        print("  Physical Properties:")
        print("   ・")
        cont = input("Press Enter to return to the main menu...")
        break
    elif userSelection == 4:
        print("This is the contents of selection 4.")
        cont = input("Press Enter to return to the main menu...")
        break

    elif userSelection == 5:
        print("This is the contents of selection 5.")
        cont = input("Press Enter to return to the main menu...")
        break

    elif userSelection == 6:
        print("This is the contents of selection 6.")
        cont = input("Press Enter to return to the main menu...")
        break

    elif userSelection == 7:
        print("This is the contents of selection 7.")
        cont = input("Press Enter to return to the main menu...")
        break

    elif userSelection == 8:
        print("This is the contents of selection 8.")
        cont = input("Press Enter to return to the main menu...")
        break

    elif userSelection == 9:
        print("Good-bye!")
        wait(1)
        system(clearScreen)
        quit()
