import class_Composors
from tkinter import *
from class_App import App

BestMusic = class_Composors.Composition()

# BestMusic.getTimeSig()  # gather info for time signature
# BestMusic.getMeasureNum() # gather info for total numbers of measures # kinda messy using this
# BestMusic.getKey()  # try enter something other than 60
# BestMusic.MinorScale2MIDI()
# BestMusic.Compose()

root = Tk()
system = App(root, BestMusic)
root.mainloop()
root.destroy()
