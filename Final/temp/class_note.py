class Note:
    def __init__(self, name="", pitch=0):  # later, can make pitch be a list of the various octaves of that note
        self.name = name
        self.pitch = pitch
    def get_name(self):
        return self.name
    def get_pitch(self):
        return self.pitch
    def get_info(self):
        info = "Note " + self.name + " has pitch " + str(self.pitch) 
        return info
    