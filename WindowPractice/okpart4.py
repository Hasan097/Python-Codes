from Tkinter import *

root = Tk()

def printName():        #OR put the key word 'event' in paranthesis
    print("Hello, my name is Taha Hasan!")

button1 = Button(root, text="print my name", command=printName)
#button1.bind("<Button-1>", printName) if ur using the 'event' thing
button1.pack()

root.mainloop()