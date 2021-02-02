import random
import tkinter as tk
import  PIL.Image, PIL.ImageTk
from tkinter import messagebox
from tkinter import *


# Main Window [Frame]
root = tk.Tk()
root.geometry('370x370')  #set the size of window
root.title('Rolling Dice') #title for window

# Top Label widgit
L1 = tk.Label(root, text="Rolling Dice", fg = "red",bg = "light gray",font = "Termina 16 bold ",width=30)
L1.pack()

# Prompt Widgett
L2 = tk.Label(root,text="Select the type of dice to roll",height=2)
L2.pack()

# Image of cube
img = PIL.ImageTk.PhotoImage(PIL.Image.open("dice1.png"))
L3=tk.Label(root, image = img)
L3.image = img
L3.pack( expand=True)

#Cube function
def Cube():
    val = random.randint(1,6)
    A1 = (f"You got: {val}")
    messagebox.showinfo("Result",A1)
btn=tk.Button(root,text="Roll Cube ",command=Cube,width=20,padx=15,pady=10,relief=RAISED)
btn.pack()

#Tetrhedron function
def Tetrahedron():
    val = random.randint(1,12)
    if val >= 1 and val <= 3:
        A1=(f"You rolled Face 1\nYou got: {val}")
        messagebox.showinfo("Result",A1)
    elif val >= 4 and val <= 6:
        A1=(f"You rolled Face 2\nYou got: {val}")
        messagebox.showinfo("Result",A1)
    elif val >= 7 and val <= 9:
        A1=(f"You rolled Face 3\nYou got: {val}")
        messagebox.showinfo("Result",A1)
    else:
        A1=(f"You rolled Face 4\nYou got: {val}")
        messagebox.showinfo("Result",A1)
btn2 = tk.Button(root,text = "Roll Tetrahedron",command=Tetrahedron,width=20,padx=15,pady=10,relief=RAISED)
btn2.pack()
root.mainloop()
