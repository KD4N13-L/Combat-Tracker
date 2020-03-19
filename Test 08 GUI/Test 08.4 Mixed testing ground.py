def assign(variable, value):
    variable = value
    return

pc1 = {"name": "blank", "initiative": 0, "dexterity": 0}

import tkinter as tk

pc1entry = tk.Tk()
lbl_e1 = tk.Label(pc1entry, text="Name").grid(row=0, stick = "w")
lbl_e2 = tk.Label(pc1entry, text="Initiative Score").grid(row=1, stick = "w")
lbl_e3 = tk.Label(pc1entry, text="Dexterity Modifier").grid(row=2, stick = "w")
ent_e11 = tk.Entry(pc1entry).grid(row=0, column=1)
ent_e22 = tk.Entry(pc1entry).grid(row=1, column=1)
ent_e33 = tk.Entry(pc1entry).grid(row=2, column=1)
pc1["name"] = ent_e11.get()
pc1["initiative"] = ent_e22.get()
pc1["dexterity"] = ent_e33.get()
button = tk.Button(pc1entry, text = "Stop", width = 13, height = 1, command = pc1entry.destroy).grid(row=4, column=0)
pc1entry.mainloop()

print(pc1)