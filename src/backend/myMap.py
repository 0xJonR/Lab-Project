from .Projectile import Projectile
from .Character import Character
from .Location import Location, Rock
from .Weapon import Weapon, Pistol, Rifle, Shotgun, Smg
import random
#matrix[column][row]
#origin is [0][0] top left corner: right to left movement is map[+-x][row]
#up to down movement is map[x][+-y]
# going down Y is add (Map Origin is top left)
#TODO:
class myMap():

    def __init__(self, size, spawnMod):
        self.spawnmod = spawnMod
        self.world = [[0 for j in range(size)] for i in range(size)]
        for row_index, row in enumerate(self.world):
            for col_index, item in enumerate(row):
                self.world[row_index][col_index] = Location(row_index, col_index)
                #inits world full of locations
        for x in range(self.spawnmod):
            self.ran_gen()
        for x in range(10):
            self.spawn(Rock)

    def rEz(self):
        return (random.randint(0, 100), random.randint(0, 100))

    def random(self):
        return random.randint(0, 100)

    def addChar(self, dropzonex, dropzoney):
        self.world[dropzonex][dropzoney] = Character(dropzonex, dropzoney)

    def spawn(self, itemName):
        xR = self.random()
        yR = self.random()
        self.world[xR][yR] = itemName(xR, yR)

    def ran_gen(self):
        #handles spawning random items: chooses random item to spawn
        modifier = self.random()
        if 0 <= modifier < 25:
            #pistol
            self.spawn(Pistol)
        elif 25 < modifier < 50:
            #rifle
            self.spawn(Rifle)
        elif modifier >=50 and modifier < 75:
            #shotgun
            self.spawn(Shotgun)
        elif modifier >= 75:
            #smg
            self.spawn(Smg)