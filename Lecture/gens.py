class Gens:
    def __init__(self, name='Anon'):
        self.name = name
        
    def info(self):
        return self.name
    
    def equals(self, them):
        if them.name == self.name:
            return True
        else:
            return False
        
    def lessThan(self, them):
        if self.name < them.name:
            return True
        else:
            return False
    
class Choses:
    def __init__(self, tipe='boring'):
        self.tipe = tipe
        
    def info(self):
        return self.tipe