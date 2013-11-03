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
        print("General Information of Halfnium (1, 2, 4)")
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

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/1_Hafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/1_Hafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
        cont = input("\nPress Enter to return to the main menu...")
        canvas.destroy() #Clears the image from tk window
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 2: #If user types 2
        print("Discovery of Hafnium (1, 2, 3, 4, 6)")
        print()
        print("Halfnium was discovered in 1923 by Dirk Coster and George Charles von Hevesy")
        print("in Copenhagen, Denmark. Halfnium comes from the Latin name Hafnia, meaning")
        print("Copenhagen. To discover the 72nd element, Coster and von Hevesy analyzed")
        print("Zirconium ores with x-ray spectography, and they found small amounts of")
        print("Hafnium. Only 1-3 percent of a Zirconium mineral contains Hafnium. Hafnium")
        print("can be isolated into a pure form from Hafnium Tetraiodide (HfI⁴). The HfI⁴")
        print("is decomposed on a tungsten filament, which makes a crystal bar of Hafnium.")
        print("This is called the crystal bar process. The main reason Hafnium was not")
        print("discovered until 1923 is because it is extremely difficult to separate from")
        print("Zirconium ore.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 3: #If user types 3
        print("Properties of Hafnium (1, 2, 3, 4, 7)")
        print("  Physical Properties:")
        print("   ・{0:30s} 2506K (2233ºC)".format("Melting Point:"))
        print("   ・{0:30s} 4876K (8317ºC)".format("Boiling Point:"))
        print("   ・{0:30s} Solid".format("State at Room Temperature:"))
        print("   ・{0:30s} 13.31g/cm³".format("Density at Room Tempurature:"))
        print("   ・{0:30s} 2, 8, 18, 32, 10, 2".format("Electron Shell Configuration:"))
        print("   ・{0:30s} [Xe] 4f¹⁴ 5d² 6s²".format("Valence Shell Configuration:"))
        print("   ・{0:30s} Shiny".format("Lustre:"))
        print("   ・{0:30s} Silver".format("Colour:"))
        print("   ・{0:30s} Brittle".format("Malleability:"))
        print("   ・{0:30s} Ductile".format("Ductility:"))
        print("   ・{0:30s} 178.49".format("Atomic Weight:"))
        print("   ・{0:30s} 72".format("Protons:"))
        print("   ・{0:30s} 72".format("Electrons:"))
        print("   ・{0:30s} 108".format("Neutrons:"))
        print("  Chemical Properties:")
        print("   ・{0:30s} Very stable. Doesn't react with oxygen.\n                                    Doesn't react with water or acids.".format("Stability:"))
        print("   ・{0:30s} Not reactive".format("Reactivity:"))
        print("   ・{0:30s} Dust is flammable".format("Flammability:"))
        print("   ・{0:30s} Dust is explosive".format("Explosiveness:"))
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.
    
    elif userSelection == 4: #If user types 4
        print("Uses of Hafnium: (1, 4, 5, 6, 7)")
        print()
        print("Hafnium is a fairly common element. It is mainly used in nuclear reactor control")
        print("rods. A control rod controls the rate at which fission takes place inside the")
        print("nuclear reactor. Without Hafnium, it would not be possible to create nuclear")
        print("fission; it would all happen too fast and be much too dangerous. The reasons")
        print("why Hafnium is great for control rods is that it is very corrosion resistant and ")
        print("its nucleus can absord extra neutrons. Without Hafnium,  the world would have to")
        print("rely on other forms of power, such as coal, which could potentially create more")
        print("pollution than nuclear power, which would increase the rate of climate change.")
        print("Put simply, without Hafnium, climate change would happen faster. Hafnium is also")
        print("used in nuclear submarines (submarines powered by nuclear reactors). Lastly,")
        print("Hafnium is used in light bulb filaments for cameras, jet and rocket engines,")
        print("and computer chips.")
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 5: #If user types 5
        print("Processing of Hafnium: (1, 2, 3, 4, 6, 7)")
        print()
        print("Hafnium is never found on its own; it's always found with Zirconium in minerals")
        print("and ores. Hafnium is a contaminant of Zirconium, meaning that it is found with")
        print("Zirconium and can be separated. The two metals are most commonly extracted")
        print("and processed using solvent extraction, as they both have different solubilities.")
        print("The solvent extraction method is quite difficult, taking up to 3 months for the")
        print("separation process to complete, making Hafnium valuable, despite its natural")
        print("abundance in the Earth's crust.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        print("Processing of Hafnium: (1, 2, 3, 4, 6, 7)")
        print()
        print("There are 5 different ways to separate Hafnium from Zirconium, listed below.")
        print()
        print(" 1. Liquid-liquid extraction* (using their different levels of solubility)")
        print(" 2. Fractional crystallization and precipitation")
        print(" 3. Fractional distillation (using their different boiling points)")
        print(" 4. Ion migration")
        print(" 5. Electrolisis")
        print()
        print("* Chiefly used by industrial operations, also known as solvent extraction")
        cont = input("\nPress Enter to return to the main menu...")
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 6: #If user types 6
        print("This is the contents of selection 6.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 7: #If user types 7
        print("Important Hafnium Compounds: (7)")
        print()
        print("Hafnium Dioxide and Hafnium Boride are the two most common compounds involving")
        print("Hafnium. They are both used in nuclear reactor control rods. They are also used")
        print("as construction materials for jet engines, rocket engines, and guided missiles,")
        print("because Hafnium can absorb and release heat over twice as fast and Zirconium or")
        print("Titanium, the two other major elements used for those tasks.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 8: #If user types 8
        print("Sources used:")
        print()
        print("Note: Some entries may not fit on the screen.")
        print(" (1) http://www.webelements.com/hafnium/")
        print(" (2) http://www.lenntech.com/periodic/elements/hf.htm")
        print(" (3) http://www.chemicool.com/elements/hafnium.html")
        print(" (4) Knapp, Brian (2002). Francium to Polonium. Hong Kong: Atlantic Europe\n     Publishing Company Limited.")
        print(" (5) http://large.stanford.edu/courses/2011/ph241/grayson1/")
        print(" (6) http://www.swissmetalassets.com/why-we-need-hafnium.html")
        print(" (7) Mukherji, Anil K. (1970). Analytical Chemistry of Zirconium and Hafnium.\n     Oxford: Pergamon Press.")
        print(" (8) http://www.chemistryexplained.com/elements/C-K/Hafnium.html")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 9: #If user types 9
        print("Good-bye!")
        wait(1)
        system(clearScreen) #Clears the screen using the method chosen above
        quit() #Quits the program, clearing memory and threads (yay modern memory management!)
    else:
        print("Please enter a valid number (1-9).")
        wait(2)
























































while True:
    system(clearScreen)
    print("Type the number of one of the following options, and press enter,")
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
        print("General Information of Halfnium (1, 2, 4)")
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

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/1_Hafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/1_Hafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
        cont = input("\nPress Enter to return to the main menu...")
        canvas.destroy() #Clears the image from tk window
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 2: #If user types 2
        print("Discovery of Hafnium (1, 2, 3, 4, 6)")
        print("Halfnium was discovered in 1923 by Dirk Coster and George Charles von Hevesy")
        print("in Copenhagen, Denmark. Halfnium comes from the latin name Hafnia, meaning")
        print("Copenhagen. To discover the 72nd elemt, Coster and von Hevesy analyzed ores")
        print("such as zirconium with x-ray spectography. Halfnium can be isolated into a")
        print("pure form from Hafnium Tetraiodide (HfI⁴). The HfI⁴ is decomposed on a tungsten")
        print("filament, which makes a crystal bar of Hafnium. This is called the crystal")
        print("bar process. The main reason Hafnium was not discovered until 1923 is because")
        print("it is extremely difficult to obtain from Zirconium ore.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 3: #If user types 3
        print("Properties of Hafnium (1, 2, 3, 4, 7)")
        print("  Physical Properties:")
        print("   ・{0:30s} 2506K (2233ºC)".format("Melting Point:"))
        print("   ・{0:30s} 4876K (8317ºC)".format("Boiling Point:"))
        print("   ・{0:30s} Solid".format("State at Room Temperature:"))
        print("   ・{0:30s} 13.31g/cm³".format("Density at Room Tempurature:"))
        print("   ・{0:30s} 2, 8, 18, 32, 10, 2".format("Electron Shell Configuration:"))
        print("   ・{0:30s} [Xe] 4f¹⁴ 5d² 6s²".format("Valence Shell Configuration:"))
        print("   ・{0:30s} Shiny".format("Lustre:"))
        print("   ・{0:30s} Silver".format("Colour:"))
        print("   ・{0:30s} Brittle".format("Malleability:"))
        print("   ・{0:30s} 178.49".format("Atomic Weight:"))
        print("   ・{0:30s} 72".format("Protons:"))
        print("   ・{0:30s} 72".format("Electrons:"))
        print("   ・{0:30s} 108".format("Neutrons:"))
        print("  Chemical Properties:")
        print("   ・{0:30s} Mildly toxic to humans; mild irritation".format("Toxicity:"))
        print("   ・{0:30s} Dust is flammable".format("Flammability:"))
        print("   ・{0:30s} Dust is explosive".format("Explosiveness:"))
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.
    
    elif userSelection == 4: #If user types 4
        print("Uses of Hafnium: (1, 4, 5, 6, 7)")
        print()
        print("Hafnium is a fairly common element, especially considering that it is only")
        print("used in one thing: nuclear reactor control rods. A control rod controls the")
        print("rate at which fission takes place inside the nuclear reactor. Without Hafnium,")
        print("it would not be possible to create nuclear fission; it would all happen too fast")
        print("and be much to dangerous. Without Hafnium, the world would have to rely upon")
        print("other forms of power, such as coal, which could potentially create more")
        print("pollution than nuclear power, which would increase the rate of climate change.")
        print("Put simply, without Hafnium, climate change would happen faster. Hafnium is also")
        print("used in nuclear submarines (submarines powered by nuclear reactors). Lastly,")
        print("Hafnium is used in light bulb filaments for cameras, jet and rocket engines,")
        print("and computer chips.")
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above
        print("Uses of Hafnium: (1, 4, 5, 6, 7)")
        print()
        print("There are 5 different ways to separate Hafnium from Zirconium, listed below.")
        print()
        print(" 1. Liquid-liquid extraction* (using their different levels of solubility")
        print(" 2. Fractional crystallization and precipitation")
        print(" 3. Fractional distillation (using their different boiling points)")
        print(" 4. Ion migration")
        print(" 5. Electrolisis")
        print()
        print("* Chiefly used by industrial operations")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 5: #If user types 5
        print("Processing of Hafnium: (1, 2, 3, 4, 6, 7)")
        print()
        print("Hafnium is never found on it's own; it's always found with Zirconium in minerals")
        print("and ores. Hafnium is a contaminant of Zirconium, meaning that it is found with")
        print("Zirconium and can be separated. The two metals are extracted and processed using")
        print("solvent extraction, as they both have different sollubilities. The solvent")
        print("extraction method is quite difficult; it can take up to 3 months to extract the")
        print("minerals out of a few kilograms of rock, making Hafnium and Zirconium valuable.")
        print("(Hafnium much more so than Zirconium, due to it being very difficult to obtain).")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 6: #If user types 6
        print("This is the contents of selection 6.")
        cont = input("Press Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 7: #If user types 7
        print("Important Hafnium Compounds: (7)")
        print()
        print("Hafnium Dioxide and Hafnium Boride are the two most common compounds involving")
        print("Hafnium. They are both used in nuclear reactor control rods. They are also used")
        print("as construction materials for jet engines, rocket engines, and guided missiles,")
        print("because Hafnium can absorb and release heat over twice as fast and Zirconium or")
        print("Titanium, the two other major elements used for those tasks.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 8: #If user types 8
        print("Sources used:")
        print()
        print("Note: Some entries may not fit on the screen.")
        print(" (1) http://www.webelements.com/hafnium/")
        print(" (2) http://www.lenntech.com/periodic/elements/hf.htm")
        print(" (3) http://www.chemicool.com/elements/hafnium.html")
        print(" (4) Knapp, Brian (2002). Francium to Polonium. Hong Kong: Atlantic Europe\n     Publishing Company Limited.")
        print(" (5) http://large.stanford.edu/courses/2011/ph241/grayson1/")
        print(" (6) http://www.swissmetalassets.com/why-we-need-hafnium.html")
        print(" (7) Mukherji, Anil K. (1970). Analytical Chemistry of Zirconium and Hafnium.\n     Oxford: Pergamon Press.")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 9: #If user types 9
        print("Good-bye!")
        wait(1)
        system(clearScreen) #Clears the screen using the method chosen above
        quit() #Quits the program, clearing memory and threads (yay modern memory management!)
    else:
        print("Please enter a valid number (1-9).")
        wait(2)
