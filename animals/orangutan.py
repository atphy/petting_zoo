from animals import Animal
from datetime import date

class Orangutan(Animal):
    
    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True

    def feed(self):
        print(f'{self.name} was fed {self.food} and blasted off into space on {date.today().strftime("%m/%d/%Y")}')