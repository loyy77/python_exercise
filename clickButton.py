import tkinter
from tkinter import *
master=Tk()

def callback():
	messagebox("hello","helltext")

b=Button(master,text="Ok",command=callback)
b.pack()

mailloop()
