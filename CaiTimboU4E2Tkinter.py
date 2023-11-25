import tkinter

root = tkinter.Tk()

greeting = tkinter.Label(
    text = "This is a message"
    )
submitBtn = tkinter.Button(text="Click me!")

greeting.pack()
submitBtn.pack()

root.mainloop()