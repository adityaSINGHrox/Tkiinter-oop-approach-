from tkinter import *

root = Tk()

label1 = Label(root,text="name")
label2 = Label(root,text="password")

entry1 = Entry(root)
entry2 = Entry(root)


label1.grid(row=0,sticky=E)
label2.grid(row=1,sticky=E)


entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

c = Checkbutton(root,text="keep me signed in")
c.grid(columnspan=2)

root.mainloop()
