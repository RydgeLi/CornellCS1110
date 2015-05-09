'''
Created on Jul 30, 2013

@author: bailey
'''
############################################################################
# A sample program to create a multi-track, multi-channel MIDI file, 
# add notes, and write to disk.
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

# Add a class_note. addNote expects the following information:
#channel = some integer >= 0
#pitch = some integer >= 0 ... middle C = 60
#duration = 1 corresponds to a crotchet, aka a quarter class_note
#volume = 100
volume = 100 # may as well specify this here for now

# Now add the class_note.
# MyMIDI.addNote(track,channel,pitch,note_start_time,duration,volume)
MyMIDI.addNote(tracks[0],channels[0],64,start_time,1,volume)
MyMIDI.addNote(tracks[0],channels[0],62,1,1,volume)
MyMIDI.addNote(tracks[0],channels[0],60,2,1,volume)
MyMIDI.addNote(tracks[0],channels[1],48,start_time,1,volume)
MyMIDI.addNote(tracks[0],channels[1],55,1,1,volume)
MyMIDI.addNote(tracks[0],channels[1],48,2,1,volume)

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

