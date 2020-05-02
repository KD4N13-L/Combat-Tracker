import tkinter as tk
m = tk.Tk()
m.title("Creature 1")
button = tk.Button(m, text = "Stop", width = 25, command = m.destroy)
button.pack()
m.mainloop()
