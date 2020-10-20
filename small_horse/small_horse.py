from datetime import date

class Small_Horse:

    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = False
        self.slithering = False
        self.walking = True
        self.shift = shift
        self.food = food
        self.__chip_num = chip_num

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

    @property
    def full_name(self):
        return f'{self.name} the {self.species}'

    @property # The getter
    def chip_num(self):
        try:
            return self.__chip_num # Note there are 2 underscores here
        except AttributeError:
            return 0

    @chip_num.setter # The setter
    def chip_num(self, new_num):
        pass