# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:10:11 2020

@author: Adewole
"""

from tkinter import *

window = Tk()
window.title("Welcome to Adewole's app")
window.geometry('700x400')

#Adding a label
lb1 = Label(window, text="Hello", font=("Arial Bold", 20))
lb1.grid(column=0,row =0)

txt = Entry(window,width=10,)
txt.grid(column=1, row=0)
txt.focus()

def clicked():
    res = "Welcome to " + txt.get()
    lb1.configure(text= res)
#Adding a button
btn = Button(window, text="Click Me", command=clicked, bg="orange", fg="red")
btn.grid(column=2, row=0)


window.mainloop()