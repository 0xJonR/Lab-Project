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

    def reload(self): #TODO IMPLEMENT DELAY AND RELOAD
        pass
    def __str__(self):
        return self.name

class Pistol(Weapon):
    name = "pistol"
    ammo = 10
    DMG = 25
    fireRate = 0.5
    fireDistance = 10

    def __init__(self, loc):
        super().__init__(loc)


class Shotgun(Weapon):
    ammo = 5
    DMG = 420
    fireRate = 0.25
    fireDistance = 7
    def __init__(self, loc):
        super().__init__(loc)


class Rifle(Weapon):
    ammo = 30
    DMG = 300
    fireRate = 1.0
    fireDistance = 14

    def __init__(self, loc):
        super().__init__(loc)


class Smg(Weapon):
    ammo = 20
    DMG = 200
    fireRate = 1.60
    fireDistance = 10

    def __init__(self, loc):
        super().__init__(loc)

