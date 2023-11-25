import tkinter

def btnClicked():
    windowOne = tkinter.Toplevel()
    windowOne.title("The next window")
    windowOne.geometry("300x300")

    labelOne = tkinter.Label(windowOne,text="This is the next window")
    closeBtn = tkinter.Button(windowOne, text = "close window", command=windowOne.destroy)
    
    closeBtn.pack()
    labelOne.pack()

root = tkinter.Tk()
root.geometry("200x200")


nextBtn = tkinter.Button(root, text="Next window", command=btnClicked)



nextBtn.pack()

root.mainloop()