from .Location import Location
from .Weapon import Weapon

class rifle(Weapon):
    ammo = 30
    DMG = 300
    fireRate = 1.0

    def __init__(self, loc):
        super(rifle, self).__init__(loc)

