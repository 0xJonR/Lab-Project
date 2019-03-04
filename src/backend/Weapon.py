from .Projectile import Projectile
from .Location import Location

class Weapon(Location):
    def __init__(self, name, loc):
        self.name = name
        self.x = loc.x
        self.y = loc.y


    ammo = 30 #30 rounds by
    #weapons should not shoot infintely in a direction
    def shoot(self):
        #subtract one from ammo
        self.ammo -= 1
        new Projectile()
        pass

    def reload(self):
        pass
