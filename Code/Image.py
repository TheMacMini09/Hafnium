from tkinter import *

master = Tk()

canvas = Canvas(master, width = 300, height = 200)
canvas.pack(expand = YES, fill = BOTH)

gif1 = PhotoImage(file = '/Volumes/SCHOOL/SCHOOL STUFF/SNC1D/My "Favourite" Element Project/Hafnium/Images/1_Hafnium.gif')
canvas.create_image(0, 0, anchor=NW, image = gif1)
mainloop()
