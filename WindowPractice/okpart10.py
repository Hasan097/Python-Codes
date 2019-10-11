from Tkinter import *
import tkMessageBox

root = Tk()

tkMessageBox.showinfo("Window Title", "Let try our best here")

answer = tkMessageBox.askquestion("Question 1", 'Do you like Memes?')

if answer == 'yes':
    print("Miniown or the Bahb")

root.mainloop()