#!/usr/bin/python

import Tkinter
import tkMessageBox
top = Tkinter.Tk()
user="Kirt"
print "Run by " + user

# Code to add widgets will go here...
def helloCallBack():
   tkMessageBox.showinfo( "Hello Python... This is a message from " + user, "Hello World, wazzup???")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()
