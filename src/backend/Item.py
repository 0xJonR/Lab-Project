from .Projectile import Projectile
from .Location import Location
# THIS CLASS PROVIDES BASE FUNCTIONALITY FOR GUNS SUCH AS SHOOTING METHODS AND SHIT
# ALL GUNS WILL INHERIT THOSE METHODS AND JUST PROVIDE DECORATIVE SUGAR FOR HOW MUCH AMMO, DMG, ETC


# TODO add Item superclass
class Weapon(Location):
    name = "Weapon"
    ammo = 30 #30 rounds by
    dmg = 350
    fireRate = 0.5
    fireDistance = 10
    occupiesSpace = False

    def __init__(self, loc):
        #self.type = "Weapon"
        super().__init__(loc.x, loc.y)

    def spawn(self):
        pass
#    #weapons should not shoot infintely in a direction
    def shoot(self, direction): #TODO IMPLEMENT HITSCAN
        #subtract one from ammo
        self.ammo -= 1
        Projectile(self.x, self.y, self.fireDistance, direction)
        pass

    def reload(self): # TODO IMPLEMENT DELAY AND RELOAD
        pass
    def __str__(self):

        return self.name


class Pistol(Weapon):
    def __init__(self, loc):
        super().__init__(loc)
        self.name = "pistol"
        self.ammo = 10
        self.DMG = 25
        self.fireRate = 0.5
        self.fireDistance = 10


class Shotgun(Weapon):
    def __init__(self, loc):
        super().__init__(loc)
        self.ammo = 5
        self.DMG = 420
        self.fireRate = 0.25
        self.fireDistance = 7


class Rifle(Weapon):
    def __init__(self, loc):
        super().__init__(loc)
        self.ammo = 30
        self.DMG = 300
        self.fireRate = 1.0
        self.fireDistance = 14


class Smg(Weapon):

    def __init__(self, loc):
        super().__init__(loc)
        self.ammo = 20
        self.DMG = 200
        self.fireRate = 1.60
        self.fireDistance = 10
