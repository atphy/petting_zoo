from datetime import date

class Goat:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
        self.shift = shift
