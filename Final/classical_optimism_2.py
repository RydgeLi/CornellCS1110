'''
Created on Jul 30, 2013
modified from the single-note-example form midiutil
@author: bailey
'''
############################################################################
# A sample program to create a multi-track MIDI file, add notes,
# and write to disk.
############################################################################

#Import the library
from MidiFile3 import MIDIFile

# Create the MIDIFile Object
MyMIDI = MIDIFile(2) ### the integer = the number of parallel tracks available


# Add track names and tempo. The first argument to addTrackName and
# addTempo is the time to write the event. This initialises the tracks.
tracks = (0, 1)
start_time = 0

MyMIDI.addTrackName(tracks[0],start_time,"Piano")
MyMIDI.addTempo(tracks[0],start_time, 120)
#MyMIDI.addTrackName(tracks[1],start_time,"Cello")
#MyMIDI.addTempo(tracks[1],start_time, 120)

# Each track can hold multiple channels, we'll use two for now
channels = (0,1)

# Add a note. addNote expects the following information:
#channel = some integer >= 0
#pitch = some integer >= 0 ... middle C = 60
#duration = 1 corresponds to a crotchet, aka a quarter note
#volume = 100
volume = 100 # may as well specify this here for now

# Now add the note.
# MyMIDI.addNote(track,channel,pitch,note_start_time,duration,volume)
class compose:
    def __init__(self):
        self.treble_loc = start_time
        self.bass_loc = start_time
#        self.octave = dict([('C',60),('D',62),('E',64),('F',65),
#                            ('G',67),('A',69),('B',71),
#                            ('C#',61),('D#',63),('F#',66),('G#',68),('A#',70),
#                            ('Db',61),('Eb',63),('Gb',66),('Ab',68),('Bb',70)])
        self.instrs = dict([('piano',0), ('harpsichord',6), ('glock',9), ('vibes',11),
                            ('marimba',12), ('organ',19), ('guitar',24), ('bass',32),
                            ('violin',40), ('cello',42), ('harp',46), ('timps',47),
                            ('voice',54), ('trumpet',56), ('tuba',58), ('horn',60),
                            ('alto sax', 65), ('oboe',68), ('bassoon',70), ('clarinet',71),
                            ('flute',73), ('recorder',74), ('bottle',75), ('whistle',78),
                            ('fifths',96), ('halo',94), ('goblins',101), ('koto',107),
                            ('bagpipe',109), ('taiko',116), ('toms',117), ('breath',121),
                            ('seashore',122), ('bird',123), ('phone',124), ('applause',126)])
    def add2treble(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[0],pitch,self.treble_loc,length,volume)
        self.treble_loc += length # moving to next time to start a note
    def add2bass(self, pitch, length):
        MyMIDI.addNote(tracks[0],channels[1],pitch,self.bass_loc,length,volume)
        self.bass_loc += length # moving to next time to start a note
        
    def change_instr(self, time, instr):
        for channel in channels :
            MyMIDI.addProgramChange(tracks[0], channel, time, instr)

composition = compose()

composition.change_instr(start_time, composition.instrs['cello'])

composition.add2treble(64, 1)
composition.add2treble(62, 1)
composition.add2treble(60, 2)
composition.add2treble(64, 1)
composition.add2treble(62, 1)
composition.add2treble(60, 2)

composition.add2treble(67, 1)
composition.add2treble(65, 1)
composition.add2treble(64, 2)
composition.add2treble(67, 1)
composition.add2treble(65, 1)
composition.add2treble(64, 1.75)
composition.add2treble(67, 0.25)

composition.add2treble(72, 0.75)
composition.add2treble(72, 0.25)
composition.add2treble(71, 0.25)
composition.add2treble(69, 0.25)
composition.add2treble(71, 0.5)
composition.add2treble(72, 0.75)
composition.add2treble(67, 0.25)
composition.add2treble(67, 0.75)
composition.add2treble(67, 0.25)

composition.add2treble(72, 0.75)
composition.add2treble(72, 0.25)
composition.add2treble(71, 0.25)
composition.add2treble(69, 0.25)
composition.add2treble(71, 0.5)
composition.add2treble(72, 0.75)
composition.add2treble(67, 0.25)
composition.add2treble(67, 0.75)
composition.add2treble(65, 0.25)

composition.add2treble(64, 1)
composition.add2treble(62, 1)
composition.add2treble(60, 2)
composition.add2treble(64, 1)
composition.add2treble(62, 1)
composition.add2treble(60, 2)

composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)
composition.add2bass(48, 1)
composition.add2bass(55, 1)
composition.add2bass(48, 2)

# And write it to disk.
binfile = open("classical2.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

