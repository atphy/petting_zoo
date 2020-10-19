from datetime import date

class Rat_Snake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = True
        self.walking = False
        self.food = food

    def feed(self):
        print(f'{self.name} the {self.species} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"