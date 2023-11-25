import tkinter

increment = 0
timer = 0

root = tkinter.Tk()

def update():
    global timer, increment
    timer += increment
    lbl.config(text = "Time:" + str(timer))
    root.after(1000,update)

def startTime():
    global increment
    increment = 1

lbl = tkinter.Label(text = "Time:" + str(timer))
startBtn = tkinter.Button(text = "Start!", command = startTime)

lbl.pack()
startBtn.pack()
update()
root.mainloop()