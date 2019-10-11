from Tkinter import *

root = Tk()

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

chec = Checkbutton(root, text="Keep me logged in")
chec. grid(columnspan=2)


root.mainloop()