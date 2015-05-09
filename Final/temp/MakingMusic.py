import random
# Import the library
from MidiFile3 import MIDIFile
from class_note import Note
from class_chord import Chord

Octave = []  # This will be the octave going from middle C (C4) to the B above. At this point, I am limiting the music to be within this particular octave. This can be expanded in the future.
# Here the notes are initialized individually. I have only initialized the sharps rather than both the sharps and flats (i.e. C# rather than Dflat since the two notes have the same pitch. This is not proper music theory but it simplifies the code)
CMajorNotes = []

C = Note("C", 60)
Octave.append(C)
CMajorNotes.append(C)
Csharp = Note("C#", 61)
Octave.append(Csharp)
D = Note("D", 62)
Octave.append(D)
CMajorNotes.append(D)
Dsharp = Note("D#", 63)
Octave.append(Dsharp)
E = Note("E", 64)
Octave.append(E)
CMajorNotes.append(E)
F = Note("F", 65)
Octave.append(F)
CMajorNotes.append(F)
Fsharp = Note("F#", 66)
Octave.append(Fsharp)
G = Note("G", 67)
Octave.append(G)
CMajorNotes.append(G)
Gsharp = Note("G#", 68)
Octave.append(Gsharp)  
A = Note("A", 69)
CMajorNotes.append(A)
Octave.append(A)
Asharp = Note("A#", 70)
Octave.append(Asharp)
B = Note("B", 71) 
CMajorNotes.append(B)   
Octave.append(B)


CMajorChords = []

CEG = Chord(C, E, G, "major")
CMajorChords.append(CEG)
DFA = Chord(D, F, A, "minor")
CMajorChords.append(DFA)
EGB = Chord(E, G, B, "minor")
CMajorChords.append(EGB)
FAC = Chord(F, A, C, "major")
CMajorChords.append(FAC)
GBD = Chord(G, B, D, "major")
CMajorChords.append(GBD)
ACE = Chord(A, C, E, "minor")
CMajorChords.append(ACE)
BDF = Chord(B, D, F, "diminished")
CMajorChords.append(BDF)


# Create the MIDIFile Object
MyMIDI = MIDIFile(2)  # ## the integer = the number of parallel tracks available

# Add track names and tempo. The first argument to addTrackName and
# addTempo is the time to write the event. This initializes the tracks.
tracks = (0, 1)
start_time = 0

# I am naming the four parts Soprano, Alto, Tenor Bass, as in choral music
MyMIDI.addTrackName(tracks[0], start_time, "Soprano")
MyMIDI.addTempo(tracks[0], start_time, 120)
MyMIDI.addTrackName(tracks[0], start_time, "Alto")
MyMIDI.addTempo(tracks[0], start_time, 120)
MyMIDI.addTrackName(tracks[0], start_time, "Tenor")
MyMIDI.addTempo(tracks[0], start_time, 120)
MyMIDI.addTrackName(tracks[0], start_time, "Bass")
MyMIDI.addTempo(tracks[0], start_time, 120)

# Each track can hold multiple channels, we'll use four (four-part harmony)
channels = (0, 1, 2, 3)

# Add a class_note. addNote expects the following information:
# channel = some integer >= 0
# pitch = some integer >= 0 ... middle C = 60
# duration = 1 corresponds to a crotchet, aka a quarter class_note
# volume = 100
volume = 100  # may as well specify this here for now

class Compose:
    def __init__(self):
        self.sop_loc = start_time
        self.alt_loc = start_time
        self.ten_loc = start_time
        self.bass_loc = start_time
        self.sop_line = []
        self.alt_line = []
        self.ten_line = []
        self.bass_line = []
    def add2sop(self, pitch, length):
        MyMIDI.addNote(tracks[0], channels[0], pitch, self.sop_loc, length, volume)
        self.sop_loc += length  # moving to next time to start a class_note
        self.sop_line.append(pitch)
    def add2alt(self, pitch, length):
        MyMIDI.addNote(tracks[0], channels[1], pitch, self.alt_loc, length, volume)
        self.alt_loc += length  # moving to next time to start a class_note
        self.alt_line.append(pitch)
    def add2ten(self, pitch, length):
        MyMIDI.addNote(tracks[0], channels[2], pitch, self.ten_loc, length, volume)
        self.ten_loc += length  # moving to next time to start a class_note
        self.ten_line.append(pitch)
    def add2bass(self, pitch, length):
        MyMIDI.addNote(tracks[0], channels[3], pitch, self.bass_loc, length, volume)
        self.bass_loc += length  # moving to next time to start a class_note
        self.bass_line.append(pitch)
    
    def get_latest_sop(self):
        if len(self.sop_line) > 0:
            return self.sop_line[len(self.sop_line) - 1]
        else:
            return None
    def get_latest_alt(self):
        if len(self.alt_line) > 0:
            return self.alt_line[len(self.alt_line) - 1]
        else:
            return None
    def get_latest_ten(self):
        if len(self.ten_line) > 0:
            return self.ten_line[len(self.ten_line) - 1]
        else:
            return None
    def get_latest_bass(self):
        if len(self.bass_line) > 0:
            return self.bass_line[len(self.bass_line) - 1]
        else:
            return None
    
    def harmonize_note(self, note):
        harmonize = []
        for chord in CMajorChords:  # appends the correct three triads to each list
            if note in chord.notes:  # class_chord.root == class_note or class_chord.third == class_note or class_chord.fifth == class_note:
                harmonize.append(chord)
        return harmonize[random.randint(0, 2)]
    
    def compose_recursively(self, note, length, count, measure=1):
            self.add2sop(note.pitch + 12, 1)
            measure += length
            if measure >= 5:
                measure = 0
            chord = self.harmonize_note(note)
            if len(self.sop_line) == 1:  # if this is the first class_note in the sequence being harmonized, just assign the root to the bass, third to tenor, and fifth to alto.
                self.add2bass(chord.root.pitch, 1)
                self.add2ten(chord.third.pitch, 1)
                self.add2alt(chord.fifth.pitch, 1)
            else:
                if measure == 1 or measure == 3:
                    choice_1 = random.choice(chord.notes)
                    choice_2 = random.choice([x for x in chord.notes if x != choice_1])
                    choice_3 = random.choice([x for x in chord.notes if x != choice_1 and x != choice_2])
                    self.add2bass(choice_1.pitch, 1)
                    self.add2ten(choice_2.pitch, 1)
                    self.add2alt(choice_3.pitch, 1)     
            count += 1
            temp = []
            for unit in chord.notes:
                if unit != note:
                    temp.append(unit)
            next_note = temp[random.randint(0, 1)]
            next_range = [0.5, 1]
            if measure <= 1:
                next_length = next_range[random.randint(0, 1)]
            elif measure > 1 and measure < 2:
                next_length = 2 - measure
            elif measure <= 3:
                next_length = next_range[random.randint(0, 1)]
            elif  measure > 3:
                next_length = 4 - measure 
#             next_length = next_range[random.randint(0, 1)]
            if count >= 20 and note == C:  # need a reasonable coda, here I simply end the recursion if the next class_note is C
                return
            self.compose_recursively(next_note, 1, count, measure)
        
    def compose_from_melody(self, melody):  # melody is a list of tuples containing notes to be harmonized as well as their durations, this method composes a harmony for a given list of melody notes that must be provided as input
        for note in melody:
            self.add2sop(note[0].pitch + 12, note[1])  # add 12, so that the soprano sings the melody an octave higher, so the melody is heard over the other voices.
            chord = self.harmonize_note(note[0])
            if len(self.sop_line) == 1:  # if this is the first class_note in the sequence being harmonized, just assign the root to the bass, third to tenor, and fifth to alto.
                self.add2bass(chord.root.pitch, note[1])
                self.add2ten(chord.third.pitch, note[1])
                self.add2alt(chord.fifth.pitch, note[1])
            else:
                i = 0
                for unit in chord.notes:
                    if unit.pitch == self.alt_line[i]:
                        self.add2alt(unit.pitch, note[1]) 
                        i += 1
                    if unit.pitch == self.ten_line[i]:
                        self.add2ten(unit.pitch, note[1]) 
                        i += 1
                    if unit.pitch == self.bass_line[i]:
                        self.add2bass(unit.pitch, note[1]) 
                        i += 1
                    if abs(unit.pitch - self.alt_line[i]) < 8 and abs(unit.pitch - self.alt_line[i]) != 0:
                        self.add2alt(unit.pitch, note[1]) 
                        i += 1
                    if abs(unit.pitch - self.ten_line[i]) < 8 and abs(unit.pitch - self.alt_line[i]) != 0:
                        self.add2ten(unit.pitch, note[1]) 
                        i += 1
                    # #this is where I left off--not finished here yet.
            
composition = Compose()
my_melody = [(C, 1), (D, 1), (E, 1), (C, 1), (D, 1), (E, 1), (F, 1), (D, 1), (G, 1), (F, 1), (E, 1), (D, 1), (E, 1), (D, 1), (C, 1)]

# composition.compose_from_melody(my_melody)
# use the compose_recursively() to make melody
composition.compose_recursively(C, 1, 0)

print('soprano line:')
for item in composition.sop_line:
    print(item)
print('alto line:')
for item in composition.alt_line:
    print(item)
print('tenor line:')
for item in composition.ten_line:
    print(item)
print('bass line:')
for item in composition.bass_line:
    print(item)

# And write it to disk.
binfile = open("output.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()
