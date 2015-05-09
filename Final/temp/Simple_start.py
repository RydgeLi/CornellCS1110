#Simple start--this code creates class_note objects, and initializes the chords for C major. 
import random

class Note:
    def __init__(self, name = "", pitch = 0):
        self.name = name
        self.pitch = pitch
    def get_name(self):
        return self.name
    def get_pitch(self):
        return self.pitch
    def get_info(self):
        info = "Note " + self.name + " has pitch " + str(self.pitch) 
        return info
      
Octave = []#This will be the octave going from middle C (C4) to the B above. At this point, I am limiting the music to be within this particular octave. This can be expanded in the future.
#Here the notes are initialized individually. I have only initialized the sharps rather than both the sharps and flats (i.e. C# rather than Dflat since the two notes have the same pitch. This is not proper music theory but it simplifies the code)
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
CMajorNotes.append(E)
Octave.append(E)
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

class Chord:
    def __init__(self, root, third, fifth, flavor = ""):#root, third, and fifth, are all Note objects
        self.root = root
        self.third = third
        self.fifth = fifth
        self.flavor = flavor
    def chord_info(self):
        info = "root = " + self.root.name + "\nthird = " + self.third.name + "\nfifth = " + self.fifth.name + "\nThis is a " + self.flavor + " class_chord."
        return info
    
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

#A couple print statements to see how this is working so far
print(A.get_info())

print("The notes in C major are: ")
for note in CMajorNotes:
    print(note.name)

print("Here are the CMajor chords: ")    
for i in range(0, len(CMajorChords)):
    print(CMajorChords[i].chord_info())

#I'm not sure where this method will eventually go--possibly in a "compose" class?
def harmonize_note(note):
    harmonize = []
    for chord in CMajorChords: #appends the correct three triads to each list
        if chord.root == note or chord.third == note or chord.fifth == note:
            harmonize.append(chord)
    return harmonize[random.randint(0,2)].chord_info()

#randomly generates one of the three triads each time the method is called. Note that the output is different each time the program is run.  
print("Some chords to harmonize A: ")  
print(harmonize_note(A))
print(harmonize_note(A))
print(harmonize_note(A))
print(harmonize_note(A))
    
        
    

