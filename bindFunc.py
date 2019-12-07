from tkinter import *

root =Tk()

def printName(event):
    print("heyyyy it works wow")

button1 = Button(root,text="wooooooow")
button1.bind("<Button-1>",printName)
button1.pack()



root.mainloop()
