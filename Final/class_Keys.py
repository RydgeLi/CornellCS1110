import class_Triads

class Minors:
    def __init__(self, root):  # root is the number of root note of the first triad
        self.root = root
        c1 = class_Triads.Triad(self.root, self.root + 3, self.root + 7) # calculates the triads according to the root note given
        c2 = class_Triads.Triad(self.root, self.root + 3, self.root + 8)
        d1 = class_Triads.Triad(self.root + 2, self.root + 5, self.root + 8)
        d2 = class_Triads.Triad(self.root + 2, self.root + 5, self.root + 11)
        e1 = class_Triads.Triad(self.root + 3, self.root + 7, self.root + 12)
        e2 = class_Triads.Triad(self.root + 3, self.root + 8, self.root + 12)
        f1 = class_Triads.Triad(self.root + 5, self.root + 8, self.root + 12)
        f2 = class_Triads.Triad(self.root + 5, self.root + 8, self.root + 14)
        g1 = class_Triads.Triad(self.root + 7, self.root + 11, self.root + 14)
        g2 = class_Triads.Triad(self.root + 7, self.root + 12, self.root + 15)
        a1 = class_Triads.Triad(self.root + 8, self.root + 12, self.root + 15)
        a2 = class_Triads.Triad(self.root + 8, self.root + 14, self.root + 17)
        b1 = class_Triads.Triad(self.root + 11, self.root + 14, self.root + 17)
        b2 = class_Triads.Triad(self.root + 11, self.root + 14, self.root + 19)
        c1.set_friend(c2) # each triad has a friend triad that can be put together in a measure. the friend is a little variation of the original triad
        d1.set_friend(d2)
        e1.set_friend(e2)
        f1.set_friend(f2)
        g1.set_friend(g2)
        a1.set_friend(a2)
        b1.set_friend(b2)
        self.listOfTriads = [c1, c2, d1, d2, e1, e2, f1, f2, g1, g2, a1, a2, b1, b2]  # here holds the class instances of triads in his key
        self.scale = [self.root, self.root+2, self.root+3, self.root+5, self.root+7, self.root+8, self.root+11]
        self.output = self.showTriads()  # here shows the pitch number of each triads
        
    
    def showTriads (self): # this is used to store the pitch number of all the triads 
        temp = []
        for triads in self.listOfTriads:
            temp.append(triads.notes)
        self.output = temp
        return self.output

class Majors:
    def __init__(self, root): # root is the number of root note of the first triad
        self.root = root
        C1 = class_Triads.Triad(self.root, self.root+4, self.root+7) #tonic chord
        C2 = class_Triads.Triad(self.root, self.root+5, self.root+9) # calculates the triads according to the root note given
        D1 = class_Triads.Triad(self.root+2, self.root+5, self.root+9)
        D2 = class_Triads.Triad(self.root+2, self.root+5, self.root+11)
        E1 = class_Triads.Triad(self.root+4, self.root+7, self.root+11)
        E2 = class_Triads.Triad(self.root+4, self.root+7, self.root+12)
        F1 = class_Triads.Triad(self.root+5, self.root+9, self.root+12)
        F2 = class_Triads.Triad(self.root+5, self.root+9, self.root+14)
        G1 = class_Triads.Triad(self.root+7, self.root+11, self.root+14)
        G2 = class_Triads.Triad(self.root+7, self.root+12, self.root+16)
        A1 = class_Triads.Triad(self.root+9, self.root+12, self.root+16)
        A2 = class_Triads.Triad(self.root+9, self.root+12, self.root+17)
        B1 = class_Triads.Triad(self.root+11, self.root+14, self.root+17)
        B2 = class_Triads.Triad(self.root+11, self.root+14, self.root+19)
        C1.set_friend(C2) # each triad has a friend triad that can be put together in a measure. the friend is a little variation of the original triad
        D1.set_friend(D2)
        E1.set_friend(E2)
        F1.set_friend(F2)
        G1.set_friend(G2)
        A1.set_friend(A2)
        B1.set_friend(B2)
        self.listOfTriads = [C1,C2,D1,D2,E1,E2,F1,F2,G1,G2,A1,A2,B1,B2] # here holds the class instances of triads in his key
        self.scale = [self.root, self.root+2, self.root+4, self.root+5, self.root+7, self.root+9, self.root+11]
        self.output = self.showTriads() # here shows the pitch number of each triads
        
    
    def showTriads (self):
        temp = []
        for triads in self.listOfTriads:
            temp.append(triads.notes)
        self.output = temp
        return self.output
        
