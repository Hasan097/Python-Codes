from Tkinter import *

root = Tk()

photo = PhotoImage(file="icon.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()