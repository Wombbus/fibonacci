# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:29:22 2022

@author: Owner
"""
from tkinter import *

root = Tk()

root.title("fibonacci")
root.geometry("400x400")

enter = Entry(root)
lbl= Label(root, text = "fibonacci")
label_sum = Label(root)

def pattern():
    input = int(enter.get())
    sum = 0
    sum2 = 0
    firstNum = 0
    secondNum = 1
    i= 1
    while(i <= input):
        sum2 = sum+sum2
        lbl["text"] += str(sum)+" "
        label_sum["text"] = "Fibonacci sum:"+str(sum2)
        firstNum = secondNum
        secondNum = sum
        sum = firstNum + secondNum 
        i = i+1
        
        

lbl = Label(root, text = "fibonacci:")
lbl.pack()            
btn = Button(root,text = "click me to display the pattern", command= pattern)
btn.pack()
label_sum.pack()
enter.pack()

root.mainloop()