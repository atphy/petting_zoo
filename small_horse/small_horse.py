from datetime import date

class Small_Horse:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
