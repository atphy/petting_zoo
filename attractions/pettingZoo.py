class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animals):
        self.animals.extend(animals)

    @property
    def last_critter_added(self):
        return f"The most recent critter added to {self.attraction_name} is {self.animals[-1].full_name}"