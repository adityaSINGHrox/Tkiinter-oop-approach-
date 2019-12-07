from tkinter import *
import os
'''
this progarm do demonstarte that how we can implement drop down menus in tkinter
this prod also has additional features such as a status bar
this all taken from a youtube tuttorial
'''
os.system("clear")
def doNothing():
    print("nothig done")
root = Tk()
menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="file", menu= subMenu)
subMenu.add_command(label = "new proj",command = doNothing)
subMenu.add_command(label = "new ",command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "exit",command = doNothing)

editMenu = Menu(menu,tearoff=0)
menu.add_cascade(label="edit", menu= editMenu)
editMenu.add_command(label = "redo",command = doNothing)

##### toolbar #########

toolbar = Frame(root,bg="blue")
insertButt = Button(toolbar, text = "insert image",command = doNothing)
insertButt.pack(side= LEFT,padx =2,pady =2)
printButt = Button(toolbar, text ='print',command  = doNothing)
printButt.pack(side = LEFT,padx=2,pady=2)

toolbar.pack(side = TOP, fill=X)

# add status bar ###

status = Label(root,text="temproray",bd = 1,relief =SUNKEN,anchor= W )
status.pack(side = BOTTOM,fill =X)

root.mainloop()
