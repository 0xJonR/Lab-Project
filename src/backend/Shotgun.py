from .Location import Location
from .Weapon import Weapon

class Shotgun(Weapon):
    ammo = 5
    DMG = 420
    fireRate = 0.25

    def __init__(self, loc):
        super().__init__(loc)

