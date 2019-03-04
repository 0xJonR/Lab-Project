from .Weapon import Weapon
from .Location import Location


class pistol(Weapon):
    ammo = 10
    DMG = 25
    fireRate = 0.5

    def __init__(self, loc):
        super().__init__(self, loc)
