from tkinter import *


def onclick1():
    import winsound
    winsound.Beep(800, 300)


def onclick2():
    import winsound
    winsound.Beep(600, 300)


root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text="Next Page", fg="red", command=onclick1)
button2 = Button(bottomFrame, text="Previous Page", fg="green", command=onclick2)
button3 = Button(topFrame, text="Turn On", fg="blue")
button4 = Button(topFrame, text="Turn Off", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop()
