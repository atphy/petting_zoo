class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animals):
        self.animals.extend(animals)