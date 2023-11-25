import tkinter


root = tkinter.Tk()
root.geometry("200x100")

greeting = tkinter.Label(text = "Type in your name")
subitBtn=tkinter.Button(text="Submit!")
entry=tkinter.Entry()

greeting.pack()
entry.pack()
subitBtn.pack()

root.mainloop()