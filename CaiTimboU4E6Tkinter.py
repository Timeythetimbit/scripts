import tkinter
from tkinter. constants import SUNKEN
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title("CAI APP")
root.geometry('500x400')

root.iconbitmap("favicon.ico")


messagebox.askquestion("MessageBoc", "Are you a person")

messagebox.askquestion("Continue","Error, do you want to continue?", icon="error")


root.mainloop()