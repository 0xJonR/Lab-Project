from .Projectile import Projectile
from .Location import Location
#THIS CLASS PROVIDES BASE FUNCTIONALITY FOR GUNS SUCH AS SHOOTING METHODS AND SHIT
#ALL GUNS WILL INHERIT THOSE METHODS AND JUST PROVIDE DECORATIVE SUGAR FOR HOW MUCH AMMO, DMG, ETC
#TODO implement projectile functionality + HitScan


class Weapon(Location):
    ammo = 30 #30 rounds by
    dmg = 350
    fireRate = 0.5

    def __init__(self, loc):
        #self.type = "Weapon"
        super().__init__(loc.x, loc.y)

#    #weapons should not shoot infintely in a direction
    def shoot(self):
        #subtract one from ammo
        self.ammo -= 1
        Projectile(self.x, self.y)
        pass

    def reload(self):
        pass


class Pistol(Weapon):
    ammo = 10
    DMG = 25
    fireRate = 0.5

    def __init__(self, loc):
        super().__init__(self, loc)


class Shotgun(Weapon):
    ammo = 5
    DMG = 420
    fireRate = 0.25

    def __init__(self, loc):
        super().__init__(loc)


class Rifle(Weapon):
    ammo = 30
    DMG = 300
    fireRate = 1.0

    def __init__(self, loc):
        super().__init__(loc)


class Smg(Weapon):
    ammo = 20
    DMG = 200
    fireRate = 1.60

    def __init__(self, loc):
        super().__init__(loc)

