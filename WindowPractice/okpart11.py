from Tkinter import *

root = Tk()

canvas = Canvas(root, width=400, height=300)
canvas.pack()

blackline = canvas.create_line(0,0,400,100)
redline = canvas.create_line(0,300,200,50, fill="red")
greenbox = canvas.create_rectangle(25,25,130,60, fill="green")

canvas.delete(redline)
canvas.delete(ALL)

root.mainloop()