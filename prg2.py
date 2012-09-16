#!/usr/bin/python3

'''
Created on 27.11.2011

@author: savit
'''

#Простое приложение с Tk

from tkinter import Tk
from tkinter import ttk

root = Tk()

def Hello(event):
    print ("Yet another hello world")

btn = ttk.Button(root,              #родительское окно
             text="Click me")       #надпись на кнопке
btn.bind("<Button-1>", Hello)       #при нажатии ЛКМ на кнопку вызывается функция Hello
btn.pack()                          #расположить кнопку на главном окне
root.mainloop()                     #обработка внешних раздрожителей