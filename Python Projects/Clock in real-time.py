from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Softuni Basic Clock')

def clock():
    tick = strftime('%H:%M:%S %p')
    label.config(text=tick)
    label.after(1000, clock)

label = Label(root, font=('sans', 80), background='black', foreground='white')
label.pack(anchor="center")

clock()
mainloop()