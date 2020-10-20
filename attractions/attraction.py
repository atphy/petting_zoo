class Attraction:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals)'

    def __len__(self):
        return len(self.animals)

    def add(self, animals):
        self.animals.extend(animals)

    @property
    def last_critter_added(self):
        return f"The most recent critter added to {self.attraction_name} is {self.animals[-1].full_name}"