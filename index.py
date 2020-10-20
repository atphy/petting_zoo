from attractions import PettingZoo, SnakePit, Wetlands

from animals import Copperhead, Diamondback, Donkey, Fish_With_No_Eyes, Goat, Goldfish, Gorgon, Jellyfish, Llama, Mallard, Orangutan, Rat_Snake, Rattlesnake, Shark, Small_Horse

steve_url = Copperhead("Steve Url", "copperhead", "snake pellets", 1)
lucy = Diamondback("Lucy", "diamondback", "cashews", 2)
donkeh = Donkey("Donkeh", "donkey", "morning", "waffles", 3)
fsh = Fish_With_No_Eyes("Fsh", "fish with no eyes", "carrots", 4)
goatse = Goat("Goatse", "goat", "afternoon", "goat snacks", 5)
silver = Goldfish("Silver", "goldfish", "Goldfish", 6)
euryale = Gorgon("Euryale", "gorgon", "gorgonzola", 7)
peanut_butter = Jellyfish("Peanut Butter", "jellyfish", "sandwiches", 8)
miss_fuzz = Llama("Miss Fuzz", "llama", "evening", "llamagranates", 9)
mallory = Mallard("Mallory", "mallard", "mallort", 10)
tang = Orangutan("Tang", "orangutan", "midnight", "Tang", 11)
snat_rake = Rat_Snake("Snat Rake", "rat snake", "Rat Snacks(TM)", 12)
maracas = Rattlesnake("Maracas", "rattlesnake", "rattlesnacks", 13)
jaws = Shark("Jaws", "shark", "bigger boats", 14)
little_sebastian = Small_Horse("Little Sebastian", "small horse", "sunrise", "hay-zelnuts", 15)

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
snake_hole = SnakePit("The Snake Hole", "unlovable and slithery critters to avoid")
soggy_bottoms = Wetlands("Soggy Bottoms", "wet and wild critters in your area")

varmint_village.add([donkeh, goatse, miss_fuzz, tang, little_sebastian])
snake_hole.add([steve_url, lucy, euryale, snat_rake, maracas])
soggy_bottoms.add([fsh, silver, peanut_butter, mallory, jaws])

jaws.feed()