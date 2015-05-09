class Chord:
    def __init__(self, root, third, fifth, flavor=""):  # root, third, and fifth, are all Note objects
        self.root = root
        self.third = third
        self.fifth = fifth
        self.notes = [root, third, fifth]
        self.flavor = flavor
    def chord_info(self):
        info = "root = " + self.root.name + "\nthird = " + self.third.name + "\nfifth = " + self.fifth.name + "\nThis is a " + self.flavor + " chord."
        return info
    