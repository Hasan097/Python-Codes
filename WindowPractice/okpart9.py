from Tkinter import *

def donothin():
    print("Aight I won't...")

root = Tk()

# *************Main Menu**************
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)   #tells python that submenu is a SubMenu to menu and is labeled file
submenu.add_command(label="New Project...", command=donothin)
submenu.add_command(label="New...", command=donothin)
submenu.add_separator()
submenu.add_command(label="Exit", command=donothin)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Redo", command=donothin)

# ************* ToolBar ************

toolbar =Frame(root,bg="blue")
insertbutton = Button(toolbar, text="Insert an image", command=donothin)
insertbutton.pack(side=LEFT, padx=2, pady=2)
printbut = Button(toolbar, text="Print", command=donothin)
printbut.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# *********Status Bar************

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()