from tkinter import *
import os
os.system("clear")
root = Tk()

canvas = Canvas(root,width = 200,height=100)
canvas.pack()

blackline = canvas.create_line(0,0,200,50)
greenBox= canvas.create_rectangle(25,25,130,60,fill="green")
redline = canvas.create_line(0,100,200,50,fill= "red")

canvas.delete(ALL)


root.mainloop()
