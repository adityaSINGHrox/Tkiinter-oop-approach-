from tkinter import *
import os
os.system("clear")
class BuckyButtons:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text = "print mesg", command = self.printMsg)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame,text = "quit",command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMsg(self):
        print("it works")


root = Tk()

b = BuckyButtons(root)

root.mainloop()
