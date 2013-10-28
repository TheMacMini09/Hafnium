from os import system
from sys import exit
from time import sleep
from tkinter import * #for images

master = Tk() #for images
wait = sleep
#cont is the variable used when continuing to the next page or the start
cont = ""
userSelection = 0
operSys = ""
clearScreen = ''

operSys = input("Are you on (M)ac/Unix or (W)indows?").lower() #Whether to clear using clear or cls

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
    
    userSelection = int(input(" #")) #Selection of above numbers. Will print info based on number
    system(clearScreen) #Clears the screen using the method chosen above
    if userSelection == 1: #If user types 1
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

        canvas = Canvas(master, width = 300, height = 200)
        canvas.pack(expand = YES, fill = BOTH)

        gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Images/1_Hafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
        cont = input("\nPress Enter to return to the main menu...")
        canvas.destroy()
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 2: #If user types 2
        print("Discovery of Hafnium (1, 3)")
        print("Halfnium was discovered in 1923 by Dirk Coster and George Charles von Hevesy")
        print("in Copenhagen, Denmark. Halfnium comes from the latin name Hafnia, meaning")
        print("Copenhagen. To discover the 72nd elemt, Coster and von Hevesy analyzed ores")
        print("such as zirconium with x-ray spectography. Halfnium can be isolated into a ")
        print("pure form from Hafnium Tetraiodide (HfI⁴). The HfI⁴ is decomposed on a tungsten")
        print("filament, which makes a crystal bar of Hafnium. This is called the crystal")
        print("bar process.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 3: #If user types 3
        print("Properties of Hafnium")
        print("  Physical Properties:")
        print("   ・{0:30s} 2506K (2233ºC)".format("Melting Point:"))
        print("   ・{0:30s} 4876K (8317ºC)".format("Boiling Point:"))
        print("   ・{0:30s} Solid".format("State at Room Temperature:"))
        print("   ・{0:30s} 13.2g/cm³".format("Density at Room Tempurature:"))
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.
    
    elif userSelection == 4: #If user types 4
        print("This is the contents of selection 4.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 5: #If user types 5
        print("This is the contents of selection 5.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 6: #If user types 6
        print("This is the contents of selection 6.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 7: #If user types 7
        print("This is the contents of selection 7.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 8: #If user types 8
        print("This is the contents of selection 8.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 9: #If user types 9
        print("Good-bye!")
        wait(1)
        system(clearScreen) #Clears the screen using the method chosen above
        quit() #Quits the program, clearing memory and threads (yay modern memory management!)

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
    
    userSelection = int(input(" #")) #Selection of above numbers. Will print info based on number
    system(clearScreen) #Clears the screen using the method chosen above
    if userSelection == 1: #If user types 1
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
        system(clearScreen) #Clears the screen using method chosen above

    elif userSelection == 2: #If user types 2
        print("Discovery of Hafnium (1, 3)")
        print("Halfnium was discovered in 1923 by Dirk Coster and George Charles von Hevesy")
        print("in Copenhagen, Denmark. Halfnium comes from the latin name Hafnia, meaning")
        print("Copenhagen. To discover the 72nd elemt, Coster and von Hevesy analyzed ores")
        print("such as zirconium with x-ray spectography. Halfnium can be isolated into a ")
        print("pure form from Hafnium Tetraiodide (HfI⁴). The HfI⁴ is decomposed on a tungsten")
        print("filament, which makes a crystal bar of Hafnium. This is called the crystal")
        print("bar process.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above

    elif userSelection == 3: #If user types 3
        print("Properties of Hafnium")
        print("  Physical Properties:")
        print("   ・{0:30s} 2506K (2233ºC)".format("Melting Point:"))
        print("   ・{0:30s} 4876K (8317ºC)".format("Boiling Point:"))
        print("   ・{0:30s} Solid".format("State at Room Temperature:"))
        print("   ・{0:30s} 13.2g/cm³".format("Density at Room Tempurature:"))
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
    
    elif userSelection == 4: #If user types 4
        print("This is the contents of selection 4.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above

    elif userSelection == 5: #If user types 5
        print("This is the contents of selection 5.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above

    elif userSelection == 6: #If user types 6
        print("This is the contents of selection 6.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above

    elif userSelection == 7: #If user types 7
        print("This is the contents of selection 7.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above

    elif userSelection == 8: #If user types 8
        print("This is the contents of selection 8.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above

    elif userSelection == 9: #If user types 9
        print("Good-bye!")
        wait(1)
        system(clearScreen) #Clears the screen using the method chosen above
        quit() #Quits the program, clearing memory and threads (yay modern memory management!)
