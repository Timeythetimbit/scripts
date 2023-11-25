import tkinter

def btnClicked():
    greeting.config(text="You have selected " + var.get() )

root = tkinter.Tk()
root.geometry("200x200")

var = tkinter.StringVar(root,"1")


greeting = tkinter.Label(text = "Select a food")
submitBtn = tkinter.Button(
    text = "Submit", 
    command = btnClicked)


rBtnOne = tkinter.Radiobutton(text = "Pizza", variable=var, value="Similey's?")
rBtnTwo = tkinter.Radiobutton(text = "Ligma", variable=var, value="Ligma?")
rBtnThree = tkinter.Radiobutton(text = "Chicken", variable=var, value="Wow ")

greeting.pack()
rBtnOne.pack()
rBtnTwo.pack()
rBtnThree.pack()
submitBtn.pack()
root.mainloop()