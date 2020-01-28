from Tkinter import *

root = Tk()

root.title("Addition++")

def addthis(a,b):
    c = a + b
    return c

lab1 = Label(root, text="Variable 1")
lab2 = Label(root, text="Variable 2")
ent1 = Entry(root)
ent2 = Entry(root)
button1 = Button(root, text="Ok", command= result)

lab1.grid(row=0, sticky=E)
lab2.grid(row=1, sticky=E)

ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)

button1.grid(row=2)

a1 = ent1.get()
b1 = ent2.get()
c1 = addthis(a1,b1)

result = Label(root, text="Result: " + c1)
result.grid(columnspan=2)

root.mainloop()