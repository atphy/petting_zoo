from animals import Animal

class Fish_With_No_Eyes(Animal):
    
    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True