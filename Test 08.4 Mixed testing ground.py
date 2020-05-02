from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()


def callback():
    print(e.get())


master.bind('<Return>', callback)


mainloop()
