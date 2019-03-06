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
        self.size = size
        self.world = [[0 for j in range(size)] for i in range(size)]
        for row_index, row in enumerate(self.world):
            for col_index, item in enumerate(row):
                self.world[row_index][col_index] = Location(row_index, col_index)
                #inits world full of locations
        for x in range(self.spawnmod):
            self.ran_gen()
        for x in range(10):
            self.spawn(Rock)
    def getLoc(self, x, y):
        pass
    def rEz(self):
        return random.randint(1, self.size-1), random.randint(1, self.size-1)

    def random(self):
        return random.randint(1, self.size - 1)

    def addChar(self, dropzonex, dropzoney):
        self.world[dropzonex][dropzoney] = Character(dropzonex, dropzoney)

    def spawn(self, itemName):
        xR = self.random()
        yR = self.random()
        self.world[xR][yR] = itemName

    def ran_gen(self):
        #handles spawning random items: chooses random item to spawn
        modifier = self.random()
        loc = Location(self.random(), self.random())
        if 0 <= modifier < 25:
            #pistol
            self.spawn(Pistol(loc))
        elif 25 < modifier < 50:
            #rifle
            self.spawn(Rifle(loc))
        elif modifier >=50 and modifier < 75:
            #shotgun
            self.spawn(Shotgun(loc))
        elif modifier >= 75:
            #smg
            self.spawn(Smg(loc))