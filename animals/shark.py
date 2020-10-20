from animals import Animal
from datetime import date

class Shark(Animal):
    
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(f'{self.name} was fed {self.food} and given a cold Naragansett on {date.today().strftime("%m/%d/%Y")}')