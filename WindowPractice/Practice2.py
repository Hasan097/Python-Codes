from Tkinter import *
import time

def playgame():
    for i in range(10):
        print(".")
        time.sleep(1)

root = Tk()

frame = Frame(root, bg="black")
lab1 = Label(frame, text="Name")
lab2 = Label(frame, text="Password")
ent1 = Entry(frame)
ent2 = Entry(frame)
button = Button(frame, text="Press here", command=playgame)

frame.pack()
lab1.grid(row=0,sticky=E)
lab2.grid(row=1,sticky=E)
ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)
button.grid(columnspan=2)

root.mainloop()