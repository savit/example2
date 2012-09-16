#!/usr/bin/python3

'''
Created on 27.11.2011
@author: savit
'''
from tkinter import Button, Tk

#Простое приложение с Tk, с автоматческим расположением pack()

root = Tk()
Button(root, text = '1').pack(side = 'left')
Button(root, text = '2').pack(side = 'top')
Button(root, text = '3').pack(side = 'right')
Button(root, text = '4').pack(side = 'bottom')
Button(root, text = '5').pack(fill = 'both')
root.mainloop()