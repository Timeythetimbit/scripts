from tkinter import *
click = 0
amount = 1
cost1 = 50
cost2 = 250
cost3 = 500
cost4 = 1000
cost5 = 5000
window = Tk()
root = Tk()
window.title("Alien CLicker By Timey")
window.geometry('380x425')
def resize():
   w = 500
   h = 500
   root.geometry(f"{w}x{h}")
my_button = Button(root, text="Resize", command=resize)
my_button.pack(pady=20)
lbl = Label(window, text="Start Clicking!")
lbl.grid(column = 1, row = 0)
milk_man = Label(window, text = "$"+str(cost1))
milk_man.grid(column = 1, row = 10)
ingredients1 = Label(window, text = "$"+str(cost2))
ingredients1.grid(column = 1, row = 20)
grandmas = Label(window, text="$"+str(cost3))
grandmas.grid(column = 1, row = 30)
factory = Label(window, text = "$"+str(cost4))
factory.grid(column = 1, row = 40)
bomb = Label(window, text = "$"+str(cost5))
bomb.grid(column = 1, row = 50)
def clicked():
    global click
    global amount
    click += amount
    lbl.configure(text= click)
def buy1():    
    global amount    
    global click    
    global cost1    
    if click >= cost1:    
      click = click - cost1    
      amount = amount + 1    
      cost1 = round(cost1*1.15)   
      milk_man.configure(text="$"+str(cost1))
      lbl.configure(text=click)
def buy2():    
    global amount    
    global click    
    global cost2    
    if click >= cost2:   
      click = click - cost2    
      amount = amount + 5    
      cost2 = round(cost2*1.15)    
      ingredients1.configure(text="$"+str(cost2))    
      lbl.configure(text=click)
def buy3():   
    global amount   
    global click    
    global cost3    
    if click >= cost3:    
      click = click - cost3    
      amount = amount + 10    
      cost3 = round(cost3*1.15)    
      grandmas.configure(text="$"+str(cost3))    
      lbl.configure(text=click)
def buy4():   
    global amount   
    global click    
    global cost4   
    if click >= cost4:    
      click = click - cost4    
      amount = amount + 20    
      cost4 = round(cost4*1.50)    
      factory.configure(text="$"+str(cost4))    
      lbl.configure(text=click)
def buy5():
   global amount
   global click
   global cost5
   if click >= cost5:
      click = click-cost5
      amount = amount + 1000000
      cost5 = round(cost5*2.5)
      bomb.configure(text="$"+str(cost5))
      lbl.configure(text=click)

cookie = PhotoImage(file='Space.png')

btn = Button(window, image=cookie, command = clicked)
btn.grid(column = 100, row = 0)
btn = Button(window, text = "Milk", command = buy1)
btn.grid(column = 100, row = 10)
btn = Button(window, text ="Ingredients", command = buy2)
btn.grid(column = 100, row = 20)
btn = Button(window, text = "Grandmas", command = buy3)
btn.grid(column = 100, row = 30)
btn = Button(window, text = "Factory", command = buy4)
btn.grid(column = 100, row = 40)
btn = Button(window, text = "BOMB!", command = buy5)
btn.grid(column = 100, row = 50)



root.mainloop()
window.mainloop()