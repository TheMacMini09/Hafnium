from os import system
from sys import exit
from time import sleep
from math import ceil
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
    print(" (9) Quiz!!")
    print(" (10) Quit the program")
    
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

        canvas = Canvas(master, width = 320, height = 320)
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

        canvas = Canvas(master, width = 365, height = 250)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/2_DiscoveryOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/2_DiscoveryOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
        cont = input("\nPress Enter to return to the main menu...")
        canvas.destroy() #Clears the image from tk window
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
        
        canvas = Canvas(master, width = 320, height = 350)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/3_PropertiesOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/3_PropertiesOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
            
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above
        
        print("Properties of Hafnium (1, 2, 3, 4, 7)")
        print()
        print("  Nuclear Properties:")
        print("   Hafinum's nucleus is very good at capturing stray neutrons, which is why it")
        print("   is used in nuclear reactor control rods; it can limit the amount of fission")
        print("   taking place in the reactor. Nuclear raections wouldn't be possible without")
        print("   Hafnium; there would be no way to limit the reaction.")
        cont = input("\nPress enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        canvas.destroy()
        break #Breaks current loop, to go to menu 2.
    
    elif userSelection == 4: #If user types 4
        print("Uses of Hafnium: (1, 4, 5, 6, 7, 9)")
        print()
        print("Hafnium is a fairly common element. It is mainly used in nuclear reactor control")
        print("rods. A control rod controls the rate at which fission takes place inside the")
        print("nuclear reactor. Without Hafnium, it would not be possible to create nuclear")
        print("fission; it would all happen too fast and be much too dangerous. The reasons")
        print("why Hafnium is great for control rods is that it is very corrosion resistant and")
        print("its nucleus can absord extra neutrons. Without Hafnium,  the world would have to")
        print("rely on other forms of power, such as coal, which could potentially create more")
        print("pollution than nuclear power, which would increase the rate of climate change.")
        print("Put simply, without Hafnium, climate change would happen faster. Hafnium is also")
        print("used in nuclear submarines (submarines powered by nuclear reactors). Lastly,")
        print("Hafnium is used in light bulb filaments for cameras, jet and rocket engines,")
        print("and computer chips. Hafnium Boride, Hafnium Nitride, and Halnium Oxide are")
        print("compounds with interesting properties; they reflect heat away from themselves.")
        print("They are used to line the inside of high-temperature ovens and kilns.")

        canvas = Canvas(master, width = 300, height = 240)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/4_UsesOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/4_UsesOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
        cont = input("\nPress Enter to continue...")
        
        system(clearScreen) #Clears the screen using method chosen above
        
        print("Uses of Hafnium: (1, 4, 5, 6, 7, 9)")
        print()
        print("Hafnium is used in many careers, though many of them use Hafnium indirectly.")
        print("Many professionals do not even know that they are working around Hafnium.")
        print()
        print("Jobs that use Hafnium, or a product of Hafnium, could include a worker in a")
        print("nuclear reactor, because a nuclear reactor requires Hafnium in control rods.")
        print("Another job that could require Hafnium is a potter, because they requireHafnium")
        print("for their kilns to fire their pottery. Also, professionals using computers will")
        print("most likely be using Hafnium in their computer chips. Photographers will also be")
        print("using Hafnium in their flash bulbs, though again, indirectly.")
        print()
        print("Some jobs that use Hafnium directly are Hafnium miners, in countries like")
        print("Australia, Malawi, Brazil, and the U.S. The main producers of Hafnium are")
        print("Australia and South Africa.")
        cont = input("\nPress Enter to return to the main menu...")

        canvas.destroy()
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

        canvas = Canvas(master, width = 320, height = 235)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/5_ProcessingOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/5_ProcessingOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
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
        canvas.destroy()
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 6: #If user types 6
        print("Safety Hazards and Necesary Precautions:")
        print()
        print("Hafnium is very useful, though it is also dangerous. Hafnium and its compounds")
        print("are toxic, and most dangerous when inhaled. Powdered Hafnium metal is explosive")
        print("and flammable, and can spontaneously combust. Overexposure of Hafnium, as long")
        print("as not inhaled, can cause inflamation and irritation of human tissue. When")
        print("working with or around powdered Hafnium, there should be no oxidising materials")
        print("and it should not be near any sources of heat or sparks. When working with any")
        print("form of Hafnium, wear gloves and/or PPE, to avoid contact with skin. If Hafnium")
        print("comes in contact with skin or eyes, rinse thoroughly with water and seek")
        print("medical attention immediately. If ingested, drink 1-2 glasses of water or milk")
        print("and seek medical attention.  If inhaled, immediately return to fresh air, and")
        print("apply oxygen if there is difficulty breathing and seek medical attention.")
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above
        print(" Safety Hazards and Necesary Precautions:")
        print()
        print("If powdered Hafnium ignites, which it may do unexpectedly at room temperature,")
        print("use appropriate metal fire-extinguishing material, such as a type D fire")
        print("exteinguisher. \033[1m\033[31mDO NOT USE WATER. \033[0m\033[31mDo not spray water on burning, chips of,")
        print("or powdered Hafnium, as a violent explosion may occur.\033[0m The smaller the particle")
        print("is, the greater the risk of explosion and combustion. Carbon Dioxide will not")
        print("effectively extinguish a Hafnium fire. Firefighters should wear contained")
        print("breathing apparatuses and gloves to avoid contact and inhalation of dust.")
        print("If there is a Hafnium spill, quickly isolate the spill to avoid environmental")
        print("damage. Hafnium should be stored in a cool, dry area. It should be stored in")
        print("an airtight container. Hafnium is considered a hazardous waste flammable")
        print("solid. Dispose of in accordance to local, provincial, and federal laws.")
        cont = input("\nPress enter to return to the main menu...")
        system(clearScreen)
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
        print(" (9) www.miningoilgasjobs.com.au/mining/rocks,\n     -metals---gems/metals/hafnium.aspx")
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above\
        print("Image sources:")
        print()
        print("Images are listed as they appear; for instace, image source (1) is for the first")
        print("menu selection, (2) being for the second, and so on.")
        print()
        print(" (1) http://www.webelements.com/_media/elements/element-pics-theo/72_Hf_3.jpg")
        print(" (2) http://www.radiochemistry.org/nuclearmedicine/pioneers/images/hevesy.jpg")
        print(" (3) http://upload.wikimedia.org/wikipedia/commons/1/1e/Electron_shell_072_hafnium.png")
        print(" (4) http://www.chemicool.com/elements/images/300-nuclear-sub.jpg")
        print(" (5) http://upload.wikimedia.org/wikipedia/commons/9/92/Zirconium_crystal_bar_and_1cm3_cube.jpg")
        print(" (10) http://www.youtube.com/watch?v=zsTRxXvQY0s")
        con = input("\nPress Enter to return to the main menu...")
        system(clearScreen)
        break #Breaks current loop, to go to menu 2.

    elif userSelection == 9:
        print("Welcome to the quiz on Hafnium! This will test your knowledge on the information")
        print("You will only get one chance on every question, and the answers will be given at")
        ready = input("the end of the quiz. Ready to begin? y/n: ").lower()
        if ready == "y":
            print()
            print("OK, lets begin!")
            wait(1)
            system(clearScreen)
            print("Let's start easy. What is the atomic mass/number of Hafnium?")
            print(" (1) 54")
            print(" (2) 72")
            print(" (3) 93")
            print(" (4) 86")
            quizQ1 = input(" #")
            print("\nOK, let's move on!")
            wait(1)
            system(clearScreen)
            print("Again, let's do an easy one. What is the symbol of Hafnium?")
            print(" (1) Hf")
            print(" (2) Ha")
            print(" (3) He")
            print(" (4) Hn")
            quizQ2 = input(" #")
            print("\nLet's continue!")
            wait(1)
            system(clearScreen)
            print("Hmm, lets try something a little harder. Which group and period is Hafnium")
            print("located in the Periodic Table of the Elements?")
            print()
            print("     Group, Period")
            print(" (1)   3      8")
            print(" (2)   8      3")
            print(" (3)   4      6")
            print(" (4)   6      4")
            quizQ3 = input(" #")
            print("Think you got that one? Let's see what's next!")
            wait(1)
            system(clearScreen)
            print("I hope you studied for this one. Who discovered Hafnium?")
            print()
            print(" (1) Charles von Hevesy, Dirk Coster")
            print(" (2) Dirk Coster")
            print(" (3) Charles von Hevesy")
            print(" (4) Galileo Galilee")
            quizQ4 = input(" #")
            print("You better not have picked 4...")
            wait(1)
            system(clearScreen)
            print("Now for some harder questions! What is the main use of Hafnium?")
            print()
            print(" (1) Micro Chips")
            print(" (2) Nuclear reactor control rods")
            print(" (3) High-heat furnaces/kilns")
            print(" (4) Lightbulb filaments for cameras")
            quizQ5 = input(" #")
            print("Good luck...")
            wait(1)
            system(clearScreen)
            print("Where is Hafnium NOT mined?")
            print(" (1) Australia")
            print(" (2) United States")
            print(" (3) Brazil")
            print(" (4) South Africa")
            quizQ6 = input(" #")
            print("You thought that one was hard? Ha. Haha. Hahahahahahahahahaha.")
            wait(2)
            system(clearScreen)
            print("What is the main way to process Hafnium?")
            print(" (1) Solvent extraction")
            print(" (2) Fractional crystallization")
            print(" (3) Fractional distillation")
            print(" (4) Ion migration")
            quizQ7 = input(" #")
            print("Sorry 'bout that one. Maybe I'll go easy on you next...")
            wait(2)
            system(clearScreen)
            print("Powdered Hafnium is ___________")
            print(" (1) Explosive")
            print(" (2) Flammable")
            print(" (3) Toxic when inhaled")
            print(" (4) All of the above")
            quizQ8 = input(" #")
            print("Almost done!")
            wait(1)
            system(clearScreen)
            print("What are the two most import compounds involving Hafnium?")
            print(" (1) Hafnium Dioxide and Hafnium Boride")
            print(" (2) Hafnium Carbide and Hafnium Dioxide")
            print(" (3) Hafnium Trisulphate and Hafnium Trihalide")
            print(" (4) Hafnium Tricarbibe and Hafnium Quadroxide")
            quizQ9 = input(" #")
            print("Hope you got the last question.")
            wait(1)
            system(clearScreen)
            print("Alright, here are your results:")

            totalQuizCorrect = 0
            
            if quizQ1 == "2":
                print("Congratulations! Question 1 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 1 is incorrect. The atomic mass of Hafnium is:")
                print(" (2) 72")
                wait(2)
                print()
            if quizQ2 == "1":
                print("Congratulations! Question 2 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 2 was incorrect. The symbol of Hafnium is:")
                print(" (1) Hf")
                wait(2)
                print()
            if quizQ3 == "3":
                print("Congratulations! Question 3 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 3 was incorrect. The group and period of Hafnium is:")
                print(" (3) Group: 4, Period: 6")
                wait(2)
                print()
            if quizQ4 == "1":
                print("Congratulations! Question 4 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 4 was incorrect. The discoverers of Hafnium were:")
                print(" (1) Charles von Hevesy, Dirk Coster")
                wait(2)
                print()
            if quizQ5 == "2":
                print("Congratulations! Question 5 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 5 was incorrect. The main use for Hafnium is:")
                print(" (2) Nuclear Reactor Control Rods")
                wait(2)
                print()
            if quizQ6 == "4":
                print("Congratulations! Question 6 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 6 was incorrect. Hafnium is NOT mined in:")
                print(" (4) South Africa")
                wait(2)
                print()
            if quizQ7 == "1":
                print("Congratulations! Question 7 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 7 was incorrect. The main way to process Hafnium is:")
                print(" (1) Solvent extraction")
                wait(2)
                print()
            if quizQ8 == "4":
                print("Congratulations! Question 8 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 8 was incorrect. Powdered Hafnium is:")
                print(" (4) All of the above (explosive, flammable, toxic when inhaled)")
                wait(2)
                print()
            if quizQ9 == "1":
                print("Congratulations! Question 9 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 9 was incorrect. The 2 most import Hafnium compounds are")
                print(" (1) Hafnium Dioxide and Hafnium Boride")
                wait(2)
                print()
            print("Your quiz total is",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".")
            print(str(totalQuizCorrect) + "/9, or", str(ceil(totalQuizCorrect/9*100)) + "%")
            wait(1)
            cont = input("Press Enter to return to the main menu...")
            break
        else:
            print()
            print("OK, returning you to the main menu...")
            wait(1)
            break

    elif userSelection == 10: #If user types 9
        print("Good-bye!")
        
        canvas = Canvas(master, width = 300, height = 200)
        canvas.pack(expand = YES, fill = BOTH)

        imagelist = ["Images/explosion/frame_000.gif","Images/explosion/frame_001.gif","Images/explosion/frame_002.gif","Images/explosion/frame_003.gif","Images/explosion/frame_004.gif","Images/explosion/frame_005.gif","Images/explosion/frame_006.gif","Images/explosion/frame_007.gif","Images/explosion/frame_007.gif","Images/explosion/frame_008.gif","Images/explosion/frame_009.gif","Images/explosion/frame_010.gif","Images/explosion/frame_011.gif","Images/explosion/frame_012.gif","Images/explosion/frame_013.gif","Images/explosion/frame_014.gif","Images/explosion/frame_015.gif","Images/explosion/frame_016.gif","Images/explosion/frame_017.gif","Images/explosion/frame_018.gif","Images/explosion/frame_019.gif","Images/explosion/frame_020.gif","Images/explosion/frame_021.gif","Images/explosion/frame_022.gif","Images/explosion/frame_023.gif","Images/explosion/frame_024.gif","Images/explosion/frame_025.gif","Images/explosion/frame_026.gif","Images/explosion/frame_027.gif","Images/explosion/frame_028.gif","Images/explosion/frame_029.gif","Images/explosion/frame_030.gif","Images/explosion/frame_031.gif","Images/explosion/frame_032.gif","Images/explosion/frame_033.gif","Images/explosion/frame_034.gif","Images/explosion/frame_035.gif","Images/explosion/frame_036.gif","Images/explosion/frame_037.gif","Images/explosion/frame_038.gif","Images/explosion/frame_039.gif","Images/explosion/frame_040.gif","Images/explosion/frame_041.gif","Images/explosion/frame_042.gif","Images/explosion/frame_043.gif","Images/explosion/frame_044.gif","Images/explosion/frame_045.gif","Images/explosion/frame_046.gif","Images/explosion/frame_047.gif","Images/explosion/frame_048.gif","Images/explosion/frame_049.gif","Images/explosion/frame_050.gif","Images/explosion/frame_051.gif","Images/explosion/frame_052.gif","Images/explosion/frame_053.gif","Images/explosion/frame_054.gif","Images/explosion/frame_055.gif","Images/explosion/frame_056.gif","Images/explosion/frame_057.gif","Images/explosion/frame_058.gif","Images/explosion/frame_059.gif","Images/explosion/frame_060.gif","Images/explosion/frame_061.gif","Images/explosion/frame_062.gif","Images/explosion/frame_063.gif","Images/explosion/frame_064.gif","Images/explosion/frame_065.gif","Images/explosion/frame_066.gif","Images/explosion/frame_067.gif","Images/explosion/frame_068.gif","Images/explosion/frame_069.gif"]

        photo = PhotoImage(file=imagelist[0])
        width = photo.width()
        height = photo.height()
        canvas = Canvas(width=width, height=height)
        canvas.pack()

        giflist = []
        for imagefile in imagelist:
            photo = PhotoImage(file=imagefile)
            giflist.append(photo)

        for k in range(0, 1):
            for gif in giflist:
                canvas.delete(ALL)
                canvas.create_image(width/2.0, height/2.0, image=gif)
                canvas.update()
                sleep(0.1)
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")

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
    print(" (9) Quiz!!")
    print(" (10) Quit the program")
    
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

        canvas = Canvas(master, width = 320, height = 320)
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

        canvas = Canvas(master, width = 365, height = 250)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/2_DiscoveryOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/2_DiscoveryOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
        cont = input("\nPress Enter to return to the main menu...")
        canvas.destroy() #Clears the image from tk window
        system(clearScreen) #Clears the screen using method chosen above

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
        
        canvas = Canvas(master, width = 320, height = 350)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/3_PropertiesOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/3_PropertiesOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
            
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above
        
        print("Properties of Hafnium (1, 2, 3, 4, 7)")
        print()
        print("  Nuclear Properties:")
        print("   Hafinum's nucleus is very good at capturing stray neutrons, which is why it")
        print("   is used in nuclear reactor control rods; it can limit the amount of fission")
        print("   taking place in the reactor. Nuclear raections wouldn't be possible without")
        print("   Hafnium; there would be no way to limit the reaction.")
        cont = input("\nPress enter to return to the main menu...")
        system(clearScreen) #Clears the screen using method chosen above
        canvas.destroy()
    
    elif userSelection == 4: #If user types 4
        print("Uses of Hafnium: (1, 4, 5, 6, 7, 9)")
        print()
        print("Hafnium is a fairly common element. It is mainly used in nuclear reactor control")
        print("rods. A control rod controls the rate at which fission takes place inside the")
        print("nuclear reactor. Without Hafnium, it would not be possible to create nuclear")
        print("fission; it would all happen too fast and be much too dangerous. The reasons")
        print("why Hafnium is great for control rods is that it is very corrosion resistant and")
        print("its nucleus can absord extra neutrons. Without Hafnium,  the world would have to")
        print("rely on other forms of power, such as coal, which could potentially create more")
        print("pollution than nuclear power, which would increase the rate of climate change.")
        print("Put simply, without Hafnium, climate change would happen faster. Hafnium is also")
        print("used in nuclear submarines (submarines powered by nuclear reactors). Lastly,")
        print("Hafnium is used in light bulb filaments for cameras, jet and rocket engines,")
        print("and computer chips. Hafnium Boride, Hafnium Nitride, and Halnium Oxide are")
        print("compounds with interesting properties; they reflect heat away from themselves.")
        print("They are used to line the inside of high-temperature ovens and kilns.")

        canvas = Canvas(master, width = 300, height = 240)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/4_UsesOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/4_UsesOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
        cont = input("\nPress Enter to continue...")
        
        system(clearScreen) #Clears the screen using method chosen above
        
        print("Uses of Hafnium: (1, 4, 5, 6, 7, 9)")
        print()
        print("Hafnium is used in many careers, though many of them use Hafnium indirectly.")
        print("Many professionals do not even know that they are working around Hafnium.")
        print()
        print("Jobs that use Hafnium, or a product of Hafnium, could include a worker in a")
        print("nuclear reactor, because a nuclear reactor requires Hafnium in control rods.")
        print("Another job that could require Hafnium is a potter, because they requireHafnium")
        print("for their kilns to fire their pottery. Also, professionals using computers will")
        print("most likely be using Hafnium in their computer chips. Photographers will also be")
        print("using Hafnium in their flash bulbs, though again, indirectly.")
        print()
        print("Some jobs that use Hafnium directly are Hafnium miners, in countries like")
        print("Australia, Malawi, Brazil, and the U.S. The main producers of Hafnium are")
        print("Australia and South Africa.")
        cont = input("\nPress Enter to return to the main menu...")

        canvas.destroy()
        system(clearScreen) #Clears the screen using method chosen above

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

        canvas = Canvas(master, width = 320, height = 235)
        canvas.pack(expand = YES, fill = BOTH)

        if operSys == "m":
            gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Code/Images/5_ProcessingOfHafnium.gif')
        else:
            gif1 = PhotoImage(file = 'Images/5_ProcessingOfHafnium.gif')
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")
        
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
        system(clearScreen)
        canvas.destroy()

    elif userSelection == 6: #If user types 6
        print("Safety Hazards and Necesary Precautions:")
        print()
        print("Hafnium is very useful, though it is also dangerous. Hafnium and its compounds")
        print("are toxic, and most dangerous when inhaled. Powdered Hafnium metal is explosive")
        print("and flammable, and can spontaneously combust. Overexposure of Hafnium, as long")
        print("as not inhaled, can cause inflamation and irritation of human tissue. When")
        print("working with or around powdered Hafnium, there should be no oxidising materials")
        print("and it should not be near any sources of heat or sparks. When working with any")
        print("form of Hafnium, wear gloves and/or PPE, to avoid contact with skin. If Hafnium")
        print("comes in contact with skin or eyes, rinse thoroughly with water and seek")
        print("medical attention immediately. If ingested, drink 1-2 glasses of water or milk")
        print("and seek medical attention.  If inhaled, immediately return to fresh air, and")
        print("apply oxygen if there is difficulty breathing and seek medical attention.")
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above
        print(" Safety Hazards and Necesary Precautions:")
        print()
        print("If powdered Hafnium ignites, which it may do unexpectedly at room temperature,")
        print("use appropriate metal fire-extinguishing material, such as a type D fire")
        print("exteinguisher. \033[1m\033[31mDO NOT USE WATER. \033[0m\033[31mDo not spray water on burning, chips of,")
        print("or powdered Hafnium, as a violent explosion may occur.\033[0m The smaller the particle")
        print("is, the greater the risk of explosion and combustion. Carbon Dioxide will not")
        print("effectively extinguish a Hafnium fire. Firefighters should wear contained")
        print("breathing apparatuses and gloves to avoid contact and inhalation of dust.")
        print("If there is a Hafnium spill, quickly isolate the spill to avoid environmental")
        print("damage. Hafnium should be stored in a cool, dry area. It should be stored in")
        print("an airtight container. Hafnium is considered a hazardous waste flammable")
        print("solid. Dispose of in accordance to local, provincial, and federal laws.")
        cont = input("\nPress enter to return to the main menu...")
        system(clearScreen)

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
        print(" (9) www.miningoilgasjobs.com.au/mining/rocks,\n     -metals---gems/metals/hafnium.aspx")
        cont = input("\nPress Enter to continue...")
        system(clearScreen) #Clears the screen using method chosen above\
        print("Image sources:")
        print()
        print("Images are listed as they appear; for instace, image source (1) is for the first")
        print("menu selection, (2) being for the second, and so on.")
        print()
        print(" (1) http://www.webelements.com/_media/elements/element-pics-theo/72_Hf_3.jpg")
        print(" (2) http://www.radiochemistry.org/nuclearmedicine/pioneers/images/hevesy.jpg")
        print(" (3) http://upload.wikimedia.org/wikipedia/commons/1/1e/Electron_shell_072_hafnium.png")
        print(" (4) http://www.chemicool.com/elements/images/300-nuclear-sub.jpg")
        print(" (5) http://upload.wikimedia.org/wikipedia/commons/9/92/Zirconium_crystal_bar_and_1cm3_cube.jpg")
        print(" (10) http://www.youtube.com/watch?v=zsTRxXvQY0s")
        cont = input("\nPress Enter to return to the main menu...")
        system(clearScreen)

    elif userSelection == 9:
        print("Welcome to the quiz on Hafnium! This will test your knowledge on the information")
        print("You will only get one chance on every question, and the answers will be given at")
        ready = input("the end of the quiz. Ready to begin? y/n: ").lower()
        if ready == "y":
            print()
            print("OK, lets begin!")
            wait(1)
            system(clearScreen)
            print("Let's start easy. What is the atomic mass/number of Hafnium?")
            print(" (1) 54")
            print(" (2) 72")
            print(" (3) 93")
            print(" (4) 86")
            quizQ1 = input(" #")
            print("\nOK, let's move on!")
            wait(1)
            system(clearScreen)
            print("Again, let's do an easy one. What is the symbol of Hafnium?")
            print(" (1) Hf")
            print(" (2) Ha")
            print(" (3) He")
            print(" (4) Hn")
            quizQ2 = input(" #")
            print("\nLet's continue!")
            wait(1)
            system(clearScreen)
            print("Hmm, lets try something a little harder. Which group and period is Hafnium")
            print("located in the Periodic Table of the Elements?")
            print()
            print("     Group, Period")
            print(" (1)   3      8")
            print(" (2)   8      3")
            print(" (3)   4      6")
            print(" (4)   6      4")
            quizQ3 = input(" #")
            print("Think you got that one? Let's see what's next!")
            wait(1)
            system(clearScreen)
            print("I hope you studied for this one. Who discovered Hafnium?")
            print()
            print(" (1) Charles von Hevesy, Dirk Coster")
            print(" (2) Dirk Coster")
            print(" (3) Charles von Hevesy")
            print(" (4) Galileo Galilee")
            quizQ4 = input(" #")
            print("You better not have picked 4...")
            wait(1)
            system(clearScreen)
            print("Now for some harder questions! What is the main use of Hafnium?")
            print()
            print(" (1) Micro Chips")
            print(" (2) Nuclear reactor control rods")
            print(" (3) High-heat furnaces/kilns")
            print(" (4) Lightbulb filaments for cameras")
            quizQ5 = input(" #")
            print("Good luck...")
            wait(1)
            system(clearScreen)
            print("Where is Hafnium NOT mined?")
            print(" (1) Australia")
            print(" (2) United States")
            print(" (3) Brazil")
            print(" (4) South Africa")
            quizQ6 = input(" #")
            print("You thought that one was hard? Ha. Haha. Hahahahahahahahahaha.")
            wait(2)
            system(clearScreen)
            print("What is the main way to process Hafnium?")
            print(" (1) Solvent extraction")
            print(" (2) Fractional crystallization")
            print(" (3) Fractional distillation")
            print(" (4) Ion migration")
            quizQ7 = input(" #")
            print("Sorry 'bout that one. Maybe I'll go easy on you next...")
            wait(2)
            system(clearScreen)
            print("Powdered Hafnium is ___________")
            print(" (1) Explosive")
            print(" (2) Flammable")
            print(" (3) Toxic when inhaled")
            print(" (4) All of the above")
            quizQ8 = input(" #")
            print("Almost done!")
            wait(1)
            system(clearScreen)
            print("What are the two most import compounds involving Hafnium?")
            print(" (1) Hafnium Dioxide and Hafnium Boride")
            print(" (2) Hafnium Carbide and Hafnium Dioxide")
            print(" (3) Hafnium Trisulphate and Hafnium Trihalide")
            print(" (4) Hafnium Tricarbibe and Hafnium Quadroxide")
            quizQ9 = input(" #")
            print("Hope you got the last question.")
            wait(1)
            system(clearScreen)
            print("Alright, here are your results:")

            totalQuizCorrect = 0
            
            if quizQ1 == "2":
                print("Congratulations! Question 1 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 1 is incorrect. The atomic mass of Hafnium is:")
                print(" (2) 72")
                wait(2)
                print()
            if quizQ2 == "1":
                print("Congratulations! Question 2 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 2 was incorrect. The symbol of Hafnium is:")
                print(" (1) Hf")
                wait(2)
                print()
            if quizQ3 == "3":
                print("Congratulations! Question 3 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 3 was incorrect. The group and period of Hafnium is:")
                print(" (3) Group: 4, Period: 6")
                wait(2)
                print()
            if quizQ4 == "1":
                print("Congratulations! Question 4 is correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 4 was incorrect. The discoverers of Hafnium were:")
                print(" (1) Charles von Hevesy, Dirk Coster")
                wait(2)
                print()
            if quizQ5 == "2":
                print("Congratulations! Question 5 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 5 was incorrect. The main use for Hafnium is:")
                print(" (2) Nuclear Reactor Control Rods")
                wait(2)
                print()
            if quizQ6 == "4":
                print("Congratulations! Question 6 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 6 was incorrect. Hafnium is NOT mined in:")
                print(" (4) South Africa")
                wait(2)
                print()
            if quizQ7 == "1":
                print("Congratulations! Question 7 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 7 was incorrect. The main way to process Hafnium is:")
                print(" (1) Solvent extraction")
                wait(2)
                print()
            if quizQ8 == "4":
                print("Congratulations! Question 8 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 8 was incorrect. Powdered Hafnium is:")
                print(" (4) All of the above (explosive, flammable, toxic when inhaled)")
                wait(2)
                print()
            if quizQ9 == "1":
                print("Congratulations! Question 9 was correct!")
                totalQuizCorrect += 1
                wait(2)
                print()
            else:
                print("Sorry, question 9 was incorrect. The 2 most import Hafnium compounds are")
                print(" (1) Hafnium Dioxide and Hafnium Boride")
                wait(2)
                print()
            print("Your quiz total is",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".",end="")
            wait(0.1)
            print(".")
            print(str(totalQuizCorrect) + "/9, or", str(ceil(totalQuizCorrect/9*100)) + "%")
            wait(1)
            cont = input("Press Enter to return to the main menu...")
        else:
            print()
            print("OK, returning you to the main menu...")
            wait(1)

    elif userSelection == 10: #If user types 9
        print("Good-bye!")
        
        canvas = Canvas(master, width = 300, height = 200)
        canvas.pack(expand = YES, fill = BOTH)

        imagelist = ["Images/explosion/frame_000.gif","Images/explosion/frame_001.gif","Images/explosion/frame_002.gif","Images/explosion/frame_003.gif","Images/explosion/frame_004.gif","Images/explosion/frame_005.gif","Images/explosion/frame_006.gif","Images/explosion/frame_007.gif","Images/explosion/frame_007.gif","Images/explosion/frame_008.gif","Images/explosion/frame_009.gif","Images/explosion/frame_010.gif","Images/explosion/frame_011.gif","Images/explosion/frame_012.gif","Images/explosion/frame_013.gif","Images/explosion/frame_014.gif","Images/explosion/frame_015.gif","Images/explosion/frame_016.gif","Images/explosion/frame_017.gif","Images/explosion/frame_018.gif","Images/explosion/frame_019.gif","Images/explosion/frame_020.gif","Images/explosion/frame_021.gif","Images/explosion/frame_022.gif","Images/explosion/frame_023.gif","Images/explosion/frame_024.gif","Images/explosion/frame_025.gif","Images/explosion/frame_026.gif","Images/explosion/frame_027.gif","Images/explosion/frame_028.gif","Images/explosion/frame_029.gif","Images/explosion/frame_030.gif","Images/explosion/frame_031.gif","Images/explosion/frame_032.gif","Images/explosion/frame_033.gif","Images/explosion/frame_034.gif","Images/explosion/frame_035.gif","Images/explosion/frame_036.gif","Images/explosion/frame_037.gif","Images/explosion/frame_038.gif","Images/explosion/frame_039.gif","Images/explosion/frame_040.gif","Images/explosion/frame_041.gif","Images/explosion/frame_042.gif","Images/explosion/frame_043.gif","Images/explosion/frame_044.gif","Images/explosion/frame_045.gif","Images/explosion/frame_046.gif","Images/explosion/frame_047.gif","Images/explosion/frame_048.gif","Images/explosion/frame_049.gif","Images/explosion/frame_050.gif","Images/explosion/frame_051.gif","Images/explosion/frame_052.gif","Images/explosion/frame_053.gif","Images/explosion/frame_054.gif","Images/explosion/frame_055.gif","Images/explosion/frame_056.gif","Images/explosion/frame_057.gif","Images/explosion/frame_058.gif","Images/explosion/frame_059.gif","Images/explosion/frame_060.gif","Images/explosion/frame_061.gif","Images/explosion/frame_062.gif","Images/explosion/frame_063.gif","Images/explosion/frame_064.gif","Images/explosion/frame_065.gif","Images/explosion/frame_066.gif","Images/explosion/frame_067.gif","Images/explosion/frame_068.gif","Images/explosion/frame_069.gif"]

        photo = PhotoImage(file=imagelist[0])
        width = photo.width()
        height = photo.height()
        canvas = Canvas(width=width, height=height)
        canvas.pack()

        giflist = []
        for imagefile in imagelist:
            photo = PhotoImage(file=imagefile)
            giflist.append(photo)

        for k in range(0, 1):
            for gif in giflist:
                canvas.delete(ALL)
                canvas.create_image(width/2.0, height/2.0, image=gif)
                canvas.update()
                sleep(0.1)
        canvas.create_image(0, 0, anchor=NW, image = gif1)
        if operSys == "m":
            system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
        else:
            print("\nPlease click the window 'tk' to view image")

        wait(1)
        system(clearScreen) #Clears the screen using the method chosen above
        quit() #Quits the program, clearing memory and threads (yay modern memory management!)
    else:
        print("Please enter a valid number (1-9).")
        wait(2)
