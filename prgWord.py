#!/usr/bin/python3

'''
Created on 27.11.2011

@author: savit
'''
from tkinter import Tk, Frame, Text, Scrollbar, Button, filedialog

def Quit(ev):
    root.quit()
    
def LoadFile(ev):
    fn = filedialog.askopenfilename(filetypes = [('*.txt files', '.txt')])
    if fn == '':
        return
    textbox.delete('1.0', 'end') 
    textbox.insert('1.0', open(fn, 'rt').read())
    
def SaveFile(ev):
    fn = filedialog.asksaveasfilename(filetypes = [('*.txt files', '.txt')])
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn+=".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

root = Tk()

panelFrame = Frame(root, height = 60, bg = 'gray')
textFrame = Frame(root, height = 340, width = 600)

panelFrame.pack(side = 'top', fill = 'x')
textFrame.pack(side = 'bottom', fill = 'both', expand = 1)

textbox = Text(textFrame, font='Arial 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set



textbox.pack(side = 'left', fill = 'both', expand = 1)
scrollbar.pack(side = 'right', fill = 'y')

loadBtn = Button(panelFrame, text = 'Load')
saveBtn = Button(panelFrame, text = 'Save')
quitBtn = Button(panelFrame, text = 'Quit')

loadBtn.bind("<Button-1>", LoadFile)
saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x = 10, y = 10, width = 40, height = 40)
saveBtn.place(x = 60, y = 10, width = 40, height = 40)
quitBtn.place(x = 110, y = 10, width = 40, height = 40)

root.mainloop()