from datetime import date

class Fish_With_No_Eyes:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.slithering = False
        self.walking = False
