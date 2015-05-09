import class_Keys  # importing the external files
import errors
from MidiFile3 import MIDIFile
import random

class Composition:
    def __init__(self):  # these values are all entered by the user via the GUI
        self.TimeSig = None  # get the time signature
        self.Key = None  # on which key should the music be written? gathered from user
        self.Form = None  # for later use if we try to write certain forms of music (Sonata, Concerto, Ritornello, etc.)
        self.Genre = None  # for later use if we try to include playing techniques related to certain genre (add syncopations for Jazz, etc)
        self.flavor = None
        self.instrs = dict([('piano', 0), ('harpsichord', 6), ('glock', 9), ('vibes', 11),
                            ('marimba', 12), ('organ', 19), ('guitar', 24), ('bass', 32),
                            ('violin', 40), ('viola', 41), ('cello', 42), ('contrabass', 43), ('harp', 46), ('timps', 47),
                            ('voice', 54), ('trumpet', 56), ('tuba', 58), ('horn', 60),
                            ('alto sax', 65), ('oboe', 68), ('bassoon', 70), ('clarinet', 71),
                            ('flute', 73), ('recorder', 74), ('bottle', 75), ('whistle', 78),
                            ('fifths', 96), ('halo', 94), ('goblins', 101), ('koto', 107),
                            ('bagpipe', 109), ('taiko', 116), ('toms', 117), ('breath', 121),
                            ('seashore', 122), ('bird', 123), ('phone', 124), ('applause', 126)])  # dictionary of possible instruments, linking the string name of the instrument to its number so that it can be accessed in the Midi file
        self.MyMIDI = MIDIFile(1) 
        self.tracks = (0, 1)
        self.channels = (0, 1, 2, 3)  # four channels, (one for Soprano, Alto, Tenor, Bass)
        self.length = 20  # 20 as the default number of measures
        
    def getLength(self, number):  # 10, 20, and 30 are the possible number of measures for a piece (chosen by the user in the GUI)
        if number == "10":
            self.length = 10
        if number == "20":
            self.length = 20
        if number == "30":
            self.length = 30
        
    def getTimeSig(self, number):
        loop = True
#         print('--------------------------------------------')
#         print('There are 2 types of time signature can be chosen. Enter 3 for 3/4, or 4 for 4/4 ...')
        while loop:
            try:  # trying to handle errors with exceptions
#                 num = input()
#                 if int(num) != 3 and int(num) != 4:
                if number != 3 and number != 4:
                    raise errors.nonPositive(number)  # 3/4 and 4/4 are the only possible time signatures--raise an error if a different value is inputted.
                else:
                    loop = False
            except errors.nonPositive:  # if the error is raised print a useful message to the screen
                print('The time signature can only be 3 or 4!')
                print('Enter the number of measures you would like to have in the composition...')
                loop = True
            except ValueError:
                print('Oops, something is not right! Gotta tidy up!')
                print('Enter the number of measures you would like to have in the composition...')
                loop = True
        self.TimeSig = number
        
    def getMeasureNum(self):  # we are not currently using this method, but it was written earlier when our code was using input at the keyboard rather than a GUI
        loop = True
        print('--------------------------------------------')
        print('Enter the number of measures you would like to have in the composition...')
        while loop:
            try:  # trying to handle errors with exceptions
                num = input()
                if int(num) <= 0:
                    raise errors.nonPositive(int(num))  # again, raise an error in the event the input isn't a positive integer.
                else:
                    loop = False
            except errors.nonPositive:
                print('The measure number should be a positive integer!')
                print('Enter the number of measures you would like to have in the composition...')
                loop = True
            except ValueError:
                print('Oops, something is not right! Gotta tidy up!')
                print('Enter the number of measures you would like to have in the composition...')
                loop = True
        self.MeasureNum = num
    
    # simple methods to get the Key, flavor, and to change the instrument
    def getKey(self, number):
        self.Key = number

    def getFlavor(self, flavor):
        self.flavor = flavor

    def changeInstr(self, channel, time, instr):
        self.MyMIDI.addProgramChange(self.tracks[0], channel, time, instr)

    def Scale2MIDI(self):  # method to produce a scale
        MyMIDI = MIDIFile(1)  # create a midifile
        self.tracks = (0, 1)
        start_time = 0  # starting time is initialized to be 0
        MyMIDI.addTrackName(self.tracks[0], start_time, "Scale")
        MyMIDI.addTempo(self.tracks[0], start_time, 80)
        self.channels = (0, 1)
        volume_On = 95  # on-beats are accentuated
        volume_Off = 80  # off-beats are attenuated
        if self.flavor == "Major":
            music = class_Keys.Majors(self.Key)
        elif self.flavor == "Minor":
            music = class_Keys.Minors(self.Key)  # write the music on the key that the user has specified
        i = 0
        while i < len(music.output):  # remember music.output is a big list of ''lists of pitch numbers''
            j = 0
            while j < len(music.output[i]):
                if j == 0:  # accentuate the on the beats
                    MyMIDI.addNote(self.tracks[0], self.channels[0], music.output[i][j], start_time, 1 / 3, volume_On)
                    start_time += 1 / 3
                    j += 1
                else:  # off-beats attenuation
                    MyMIDI.addNote(self.tracks[0], self.channels[0], music.output[i][j], start_time, 1 / 3, volume_Off)
                    start_time += 1 / 3
                    j += 1
            i += 1
        binfile = open("Scale.mid", 'wb')  # write the scale to a file named "Scale.mid"
        MyMIDI.writeFile(binfile)
        binfile.close()
        print('A file named Scale.mid has been generated for you. This file contains the entire scales of the key chosen.')
    
    def Measure_rythm(self, time):  # list of lists of potential rythms that can be chosen from. Each is a full measure long.
        Rythms4 = [[1, 1 / 2, 1 / 2, 1, 1], [1 / 3, 1 / 3, 1 / 3, 1, 1, 1 / 2, 1 / 2], [1 / 2, 1 / 2, 1 / 2, 1 / 4, 1 / 4, 1 / 4, 1 / 4, 1 / 2, 1], [1 / 2, 1 / 2, 1, 1 / 2, 1 / 2, 1], [1, 1, 1, 1]]
        Rythms3 = [[1, 1, 1], [1 / 3, 1 / 3, 1 / 3, 1 / 3, 1 / 3, 1 / 3, 1 / 3, 1 / 3, 1 / 3], [1 / 2, 1 / 2, 1, 1], [1 / 4, 1 / 4, 1 / 4, 1 / 4, 1 / 2, 1 / 2, 1 / 2, 1 / 2], [1, 1 / 4, 1 / 4, 1 / 4, 1 / 4, 1 / 2, 1 / 2]]
        if time == 4:  # for each time signature, choose from the proper list of rhythms.
            rythm = random.choice(Rythms4)  
        if time == 3:
            rythm = random.choice(Rythms3)
        return rythm  # return the randomly chosen rhythm
    
    def Compose(self):
        start_time = 0  # starting time is initialized to be 0
        start_time_1 = 0
        self.MyMIDI.addTrackName(self.tracks[0], start_time, "Melody")
        self.MyMIDI.addTempo(self.tracks[0], start_time, 90)
        self.channels = (0, 1, 2, 3)
        volume_On = 110  # on-beats are accentuated
        volume_Second_On = 90  # for beats at the front of a triplet but not on the beats
        volume_Off = 50  # off-beats are attenuated
        if self.flavor == "Minor":
            music = class_Keys.Minors(self.Key)  # write the music on the key that the user has specified
        elif self.flavor == "Major":
            music = class_Keys.Majors(self.Key)
        temp = [0, 0, 0]  # variable to store the triads, each time stores a new triad hasn't stored before
        j = 0
        while j < self.length:  # j is the number of measure
            triad_1 = random.choice([ x for x in music.listOfTriads if x != temp])
            rythm = self.Measure_rythm(int(self.TimeSig))
            
            # begin to generate a whole measure for the soprano
            for k in rythm:  # grab notes for each time slots
                self.MyMIDI.addNote(self.tracks[0], self.channels[0], random.choice(triad_1.friend.notes) + 12, start_time, k, volume_Second_On)  # soprano up an octave, (generate range)
                start_time += k
#             k=0
#             while k < int(len(rythm)): # grab notes for each time slots
#                 self.MyMIDI.addNote(self.tracks[0], self.channels[0], random.choice(triad_1.friend.notes) + 12, start_time, rythm[k], volume_Second_On)
#                 start_time += rythm[k]
#                 k += 1
            # here we start to generate the notes for other 3 parts:
            i = 0
            while i < int(self.TimeSig):  # i keeps track of the beats in a full measure
                choice_1 = random.choice(triad_1.friend.notes)  # "choices" generate notes for a harmonizing triad
                choice_2 = random.choice([x for x in triad_1.friend.notes if x != choice_1])
                choice_3 = random.choice([x for x in triad_1.friend.notes if x != choice_1 and x != choice_2])
                if i == 0:  # add a chord in the alto, tenor, and bass to correspond with the first on beat
                    self.MyMIDI.addNote(self.tracks[0], self.channels[1], choice_1, start_time_1, 2, volume_Off)  # establish range--alto stays where it is, tenor down an octave, bass down two octaves
                    self.MyMIDI.addNote(self.tracks[0], self.channels[2], choice_2 - 12, start_time_1, 2, volume_Off)
                    self.MyMIDI.addNote(self.tracks[0], self.channels[3], choice_3 - 24, start_time_1, 2, volume_Off)
                    start_time_1 += 2
                    i += 2
                if i == 2:  # add a chord in the alto, tenor and bass to correspond with the second on beat
                    choice_1 = random.choice(triad_1.friend.notes)
                    choice_2 = random.choice([x for x in triad_1.friend.notes if x != choice_1])
                    choice_3 = random.choice([x for x in triad_1.friend.notes if x != choice_1 and x != choice_2])
                    if self.TimeSig == 3:  # separate code for 3/4 and 4/4 music
                        self.MyMIDI.addNote(self.tracks[0], self.channels[1], choice_1, start_time_1, 1, volume_Off)
                        self.MyMIDI.addNote(self.tracks[0], self.channels[2], choice_2 - 12, start_time_1, 1, volume_Off)
                        self.MyMIDI.addNote(self.tracks[0], self.channels[3], choice_3 - 24, start_time_1, 1, volume_Off)
                        start_time_1 += 1
                        i += 1
                    else:  # if self.TimeSig == 4:
                        self.MyMIDI.addNote(self.tracks[0], self.channels[1], choice_1, start_time_1, 2, volume_Off)
                        self.MyMIDI.addNote(self.tracks[0], self.channels[2], choice_2 - 12, start_time_1, 2, volume_Off)
                        self.MyMIDI.addNote(self.tracks[0], self.channels[3], choice_3 - 24, start_time_1, 2, volume_Off)
                        start_time_1 += 2
                        i += 2
            j += 1  # increment j to keep composing
            temp = triad_1  # update temp
            
        # add a coda after the while j loop--different code for each possible combination of flavor and time signature (4 possibilities)
        if self.flavor == "Major" and int(self.TimeSig) == 3:
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 16, start_time, 1, volume_Second_On)
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 11, start_time_1, 3, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 5, start_time_1, 3, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root + 2, start_time_1, 3, volume_Off)
            start_time += 1  # increment the start time
            start_time_1 += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 14, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 11, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 12, start_time, 3, volume_Second_On) 
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 7, start_time_1, 3, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 4, start_time_1, 3, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root, start_time_1, 3, volume_Off)
            
        elif self.flavor == "Major" and int(self.TimeSig) == 4:
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 4, start_time, 1, volume_Second_On)
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 11, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 5, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root + 2, start_time_1, 4, volume_Off)
            start_time += 1
            start_time_1 += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 16, start_time, 1, volume_Second_On)
            start_time += 1  
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 14, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 11, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 12, start_time, 4, volume_Second_On) 
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 7, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 4, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root, start_time_1, 4, volume_Off)  
            
        elif self.flavor == "Minor" and int(self.TimeSig) == 3:
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 15, start_time, 1, volume_Second_On)
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 11, start_time_1, 3, volume_Second_On)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 5, start_time_1, 3, volume_Second_On)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root + 2, start_time_1, 3, volume_Second_On)
            start_time += 1  
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 14, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 11, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 12, start_time, 3, volume_Second_On) 
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 7, start_time_1, 3, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 3, start_time_1, 3, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root, start_time_1, 3, volume_Off)
             
        elif self.flavor == "Minor" and int(self.TimeSig) == 4:
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 3, start_time, 1, volume_Second_On)
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 11, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 5, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root + 2, start_time_1, 4, volume_Off)
            start_time += 1
            start_time_1 += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 15, start_time, 1, volume_Second_On) 
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 14, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 11, start_time, 1, volume_Second_On)
            start_time += 1
            self.MyMIDI.addNote(self.tracks[0], self.channels[0], music.root + 12, start_time, 4, volume_Second_On) 
            self.MyMIDI.addNote(self.tracks[0], self.channels[1], music.root + 7, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[2], music.root + 3, start_time_1, 4, volume_Off)
            self.MyMIDI.addNote(self.tracks[0], self.channels[3], music.root, start_time_1, 4, volume_Off)  
        binfile = open("output.mid", 'wb')  # write the music to a file!
        self.MyMIDI.writeFile(binfile)
        binfile.close()


