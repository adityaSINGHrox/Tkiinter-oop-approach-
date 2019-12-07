from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side =BOTTOM)

b1 = Button(top_frame,text = "but_1")
b2 =Button(top_frame,text = "but_2")
b3 = Button(top_frame,text="but_3")
b4 = Button(bottom_frame,text ="but_4")


b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)
b4.pack(side = BOTTOM)
root.mainloop()
