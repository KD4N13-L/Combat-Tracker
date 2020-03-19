import tkinter as tk
from tkinter import Label
from tkinter import Entry
pc1entry = tk.Tk()
e1 = Label(pc1entry, text = "Name").grid(row=0)
e2 = Label(pc1entry, text = "Initiative Score").grid(row=1)
e3 = Label(pc1entry, text = "Dexterity Modifier").grid(row=2)
e11 = Entry(pc1entry)
e22 = Entry(pc1entry)
e33 = Entry(pc1entry)
e11.grid(row = 0, column = 1)
e22.grid(row = 1, column = 1)
e33.grid(row = 2, column = 1)
pc1entry.mainloop()
