from Tkinter import *

def donothin():
    print("Aight I won't...")

root = Tk()

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

root.mainloop()