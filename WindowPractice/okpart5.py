from Tkinter import *

root = Tk()

def leftclick(event):
    print("LEFT")
    
def rightclick(event):
    print("RIGHT")

def midclick(event):
    print("MIDDLE")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", midclick)
frame.bind("<Button-3>", rightclick)
frame.pack()

root.mainloop()