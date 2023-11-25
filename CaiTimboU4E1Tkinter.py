import tkinter
from tkinter import ttk
root = tkinter.Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
root.geometry('550x320')
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()