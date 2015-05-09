from tkinter import *
import tkinter.messagebox
import random
class App:
    def __init__(self, master, composer):
        self.frame = Frame(master)
        self.frame.pack()
        self.composer = composer
        self.pitchs = dict([('A', 60), ('B', 61), ('C', 62), ('D', 63),
                            ('E', 64), ('F', 65), ('G', 66)])
        
        # text to welcome (row=0, column=0)
        self.title = Label(self.frame, text="Welcome to our music system!").grid(row=0, column=0, columnspan=4)
        
        # OptionMenu for choosing time signature (row=1,column=0)
        self.time_v = StringVar()
        self.time_v.set("Time Signature")
        self.timeSig_m = OptionMenu(self.frame, self.time_v, "3/4", "4/4").grid(row=1, column=0)
        
        # OptionMenu for choosing flavor (row=1, column=1)
        self.flavor_v = StringVar()
        self.flavor_v.set("Flavor")
        self.flavor_m = OptionMenu(self.frame, self.flavor_v, "Major", "Minor").grid(row=1, column=1)
        
        # OptionMenu for choosing pitch (row=1, column=2)
        self.pitch_v = StringVar()
        self.pitch_v.set("Pitch")
        self.pitch_m = OptionMenu(self.frame, self.pitch_v, "A", "B", "C", "D", "E", "F", "G").grid(row=1, column=2)
        
        # text to show the result (row=3, column=2)
        self.my_text = StringVar()
        self.my_text.set("Please make some beautiful melody!")
        self.result = Label(self.frame, textvariable=self.my_text).grid(row=3, columnspan=4)
        
        # define some buttons including random, quartet, start, quit, and scale 
        self.random_t = Label(self.frame, text="Forget all those options! Just give me good music:").grid(row=5, columnspan=4)
        self.random = Button(self.frame, text="Feeling lucky!", command=self.random_gen).grid(row=6, column=2, columnspan=2)
        self.quartet = Button(self.frame, text="Generate Quartet", command=self.quartet_gen).grid(row=6, column=0, columnspan=2)
        self.start = Button(self.frame, text="Compose", command=self.start).grid(row=4, column=1)
        self.scale = Button(self.frame, text="Scale2MIDI", command=self.scale_gen).grid(row=4, column=2)
        self.leave = Button(self.frame, text="Quit", command=self.frame.quit).grid(row=4, column=3)

        # OptionMenu for choosing instrument for soprano (row=2, column=0)
        self.soprano_v = StringVar()
        self.soprano_v.set("Instrument for soprano")
        self.soprano_m = OptionMenu(self.frame, self.soprano_v, "viola", "contrabass", "piano", "voice", "guitar", "cello",
                                    "violin", "horn", "whistle", "halo", "seashore", "bird", "applause").grid(row=2, column=0)
        
        # OptionMenu for choosing instrument for alto (row=2, column=1)
        self.alto_v = StringVar()
        self.alto_v.set("Instrument for alto")
        self.alto_m = OptionMenu(self.frame, self.alto_v, "viola", "contrabass", "piano", "voice", "guitar", "cello",
                                 "violin", "horn", "whistle", "halo", "seashore", "bird", "applause").grid(row=2, column=1)
        
        # OptionMenu for choosing instrument for tenor (row=2, column=2)
        self.tenor_v = StringVar()
        self.tenor_v.set("Instrument for tenor")
        self.tenor_m = OptionMenu(self.frame, self.tenor_v, "viola", "contrabass", "piano", "voice", "guitar", "cello",
                                  "violin", "horn", "whistle", "halo", "seashore", "bird", "applause").grid(row=2, column=2)
        
        # OptionMenu for choosing instrument for bass (row=2, column=3)
        self.bass_v = StringVar()
        self.bass_v.set("Instrument for bass")
        self.bass_m = OptionMenu(self.frame, self.bass_v, "viola", "contrabass", "piano", "voice", "guitar", "cello",
                                 "violin", "horn", "whistle", "halo", "seashore", "bird", "applause").grid(row=2, column=3)
        
        # text to show our names :)
        self.author = Label(self.frame, text="Designed by: Rydge Li, Sarah Marie Bruno, and Letian Wang").grid(row=7, columnspan=4)
        self.length_v = StringVar()
        self.length_v.set("Length")
        self.length_m = OptionMenu(self.frame, self.length_v, '10', '20', '30').grid(row=1, column=3)
        
    # command to compose a melody
    def start(self):
        if self.time_v.get() == "3/4":
            self.composer.getTimeSig(3)
        else:
            self.composer.getTimeSig(4)

        self.composer.getKey(self.pitchs[self.pitch_v.get()])
        self.composer.getFlavor(self.flavor_v.get())
        self.composer.getLength(self.length_v.get())
        
        self.composer.changeInstr(0, 0, self.composer.instrs[self.soprano_v.get()])
        self.composer.changeInstr(1, 0, self.composer.instrs[self.alto_v.get()])
        self.composer.changeInstr(2, 0, self.composer.instrs[self.tenor_v.get()])
        self.composer.changeInstr(3, 0, self.composer.instrs[self.bass_v.get()])
        
        self.composer.Compose()
        self.my_text.set("A file named 'output.mid' has been generated for you")
        tkinter.messagebox.showinfo("Done!", "A file named 'output.mid' has been generated for you")
    
    # command to compose a melody randomly
    def random_gen(self):
        self.composer.getTimeSig(random.choice([3, 4]))
        self.composer.getKey(random.choice([60, 61, 62, 63, 64, 65, 66]))
        self.composer.getFlavor(random.choice(["Major", "Minor"]))
        self.composer.changeInstr(0, 0, self.composer.instrs['piano'])
        for i in range(1, 4):
            self.composer.changeInstr(i, 0, self.composer.instrs[random.choice(["viola", "contrabass", "piano", "cello", "guitar",
                                  "violin", "voice"])])
        self.composer.Compose()
        self.my_text.set("A file named 'output.mid' has been generated for you")
        tkinter.messagebox.showinfo("Done!", "A file named 'output.mid' has been generated for you")
    
    # command to generate a quartet
    def quartet_gen(self):
        self.composer.getTimeSig(random.choice([3, 4]))
        self.composer.getKey(random.choice([60, 61, 62, 63, 64, 65, 66]))
        self.composer.getFlavor(random.choice(["Major", "Minor"]))
        #
        self.composer.changeInstr(0, 0, self.composer.instrs["violin"])
        self.composer.changeInstr(1, 0, self.composer.instrs["viola"])
        self.composer.changeInstr(2, 0, self.composer.instrs["cello"])
        self.composer.changeInstr(3, 0, self.composer.instrs["contrabass"])
        
        self.composer.Compose()
        self.my_text.set("A file named 'output.mid' has been generated for you")
        tkinter.messagebox.showinfo("Done!", "A file named 'output.mid' has been generated for you")
    
    # command to generate the scale
    def scale_gen(self):
        if self.time_v.get() == "3/4":
            self.composer.getTimeSig(3)
        elif self.time_v.get() == "4/4":
            self.composer.getTimeSig(4)

        self.composer.getKey(self.pitchs[self.pitch_v.get()])
        self.composer.getFlavor(self.flavor_v.get())
        self.composer.getLength(self.length_v.get())
        
        self.composer.changeInstr(0, 0, self.composer.instrs[self.soprano_v.get()])
        self.composer.changeInstr(1, 0, self.composer.instrs[self.alto_v.get()])
        self.composer.changeInstr(2, 0, self.composer.instrs[self.tenor_v.get()])
        self.composer.changeInstr(3, 0, self.composer.instrs[self.bass_v.get()])
        
        self.composer.Scale2MIDI()
        self.my_text.set("A file named Scale.mid has been generated for you")
        tkinter.messagebox.showinfo("Done!", "A file named Scale.mid has been generated for you")
        
