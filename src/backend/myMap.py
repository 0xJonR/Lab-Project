from .Projectile import Projectile
from .Character import Character
from .Location import Location
from .Weapon import Weapon
import random
#matrix[column][row]
#origin is [0][0] top left corner: right to left movement is map[+-x][row]
#up to down movement is map[x][+-y]
# going down Y is add (Map Origin is top left)
# TODO : ADD SPAWNING FUNCTIONALITY
class myMap():


    def __init__(self, size):
        self.world = [[0 for j in range(size)] for i in range(size)]
        for row_index, row in enumerate(self.world):
            for col_index, item in enumerate(row):
                self.world[row_index][col_index] = Location(row_index, col_index)
                #inits world full of locations

    def rEz(self):
        return (random.randint(0, 100), random.randint(0, 100))

    def random(self):
        return random.randint(0, 100)

    def addChar(self, dropzonex, dropzoney):
        self.world[dropzonex][dropzoney] = Character(dropzonex, dropzoney)
        pass #implement new character

    def spawn(self, itemName):
        xR = self.random()
        yR = self.random()
        self.world[xR][yR] = itemName

    def ranGen(self):
        #handles spawning random items: chooses random item to spawn
        #TODO: handle case switching for different weapons
        modifier = self.random()
        return self.spawn(Weapon)



