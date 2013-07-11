import tkinter
from tkinter import *

master=Tk()

def callback():
    print("hello")
  
    
b=Button(master,text="Ok",command=callback)
b.pack()

mainloop()

