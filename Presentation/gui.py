from tkinter import *
class Fun:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.leave = Button(frame, text="QUIT", command=frame.quit)
        self.leave.pack(side=LEFT)
        self.greet = Button(frame, text="Greetings all!", command=self.greet)
        self.greet.pack(side=LEFT)
    def greet(self):
        print("Hello Sir Console!")
root = Tk()
# quest = Label(root, text="Anyone alive out there?")
fun_stuff = Fun(root)
# quest.pack()
root.mainloop()
