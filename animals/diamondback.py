from animals import Animal
from datetime import date

class Diamondback(Animal):
    
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(f'{self.name} was fed {self.food} and got called a good boy on {date.today().strftime("%m/%d/%Y")}')