from copperhead import Copperhead
from diamondback import Diamondback
from donkey import Donkey
from fish_with_no_eyes import Fish_With_No_Eyes
from goat import Goat
from goldfish import Goldfish
from gorgon import Gorgon
from jellyfish import Jellyfish
from llama import Llama
from mallard import Mallard
from orangutan import Orangutan
from rat_snake import Rat_Snake
from rattlesnake import Rattlesnake
from shark import Shark
from small_horse import Small_Horse
from attractions import PettingZoo, SnakePit, Wetlands

steve_url = Copperhead("Steve Url", "copperhead", "snake pellets")
lucy = Diamondback("Lucy", "diamondback", "cashews")
donkeh = Donkey("Donkeh", "donkey", "morning", "waffles")
fsh = Fish_With_No_Eyes("Fsh", "fish with no eyes", "carrots")
goatse = Goat("Goatse", "goat", "afternoon", "goat snacks")
silver = Goldfish("Silver", "goldfish", "Goldfish")
euryale = Gorgon("Euryale", "gorgon", "gorgonzola")
peanut_butter = Jellyfish("Peanut Butter", "jellyfish", "sandwiches")
miss_fuzz = Llama("Miss Fuzz", "llama", "evening", "llamagranates")
mallory = Mallard("Mallory", "mallard", "mallort")
tang = Orangutan("Tang", "orangutan", "midnight", "Tang")
snat_rake = Rat_Snake("Snat Rake", "rat snake", "Rat Snacks(TM)")
maracas = Rattlesnake("Maracas", "rattlesnake", "rattlesnacks")
jaws = Shark("Jaws", "shark", "bigger boats")
little_sebastian = Small_Horse("Little Sebastian", "small horse", "sunrise", "hay-zelnuts")

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
snake_hole = SnakePit("The Snake Hole", "unlovable and slithery critters to avoid")
soggy_bottoms = Wetlands("Soggy Bottoms", "wet and wild critters in your area")

varmint_village.add([donkeh, goatse, miss_fuzz, tang, little_sebastian])
snake_hole.add([steve_url, lucy, euryale, snat_rake, maracas])
soggy_bottoms.add([fsh, silver, peanut_butter, mallory, jaws])

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')