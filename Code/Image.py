import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root)

canvas.grid(row = 0, column = 0)

photo = tkinter.PhotoImage(file = '/Users/minecraft/Desktop/Untitled.gif')

canvas.create_image(0,0, image=photo)

root.mainloop()
