from .Location import Location


class Projectile(Location):
    #x y
    #hitscan
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def XYCollision(self):
        pass

    def __eq__(self, other):
        return self.x==other.x && self.y==other.y

    def projectileDistance(self, dT):
        c = new Projectile(self.x + dT, self.y + dT)
        return c

    def isCollide(self, projDistance, otherProj):
        x = projDistance.x
        y = projDistance.y
        x1 = otherProj.x
        y1 = otherProj.y
