from tkinter import *

root = Tk()

one = Label(root,text="one ",bg = "red", fg="white")
one.pack()

two = Label(root,text="two",bg="green")
two.pack(fil=X)

three = Label(root,text="three",bg="blue")
three.pack(side = LEFT,fill=Y)

root.mainloop()
