import tkinter as tk
from tkinter import Menubutton
from tkinter import Menu
from tkinter import IntVar
top = tk.Tk()
mb = Menubutton(top, text = "Alphabetical order")
mb.grid()
mb.menu = Menu (mb, tearoff = 0)
mb["menu"] = mb.menu
aVar = IntVar()
bVar = IntVar()
mb.menu.add_checkbutton(label = "A", variable = aVar)
mb.menu.add_checkbutton(label = "B", variable = bVar)
mb.pack()
top.mainloop()