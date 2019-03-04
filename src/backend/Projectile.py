from .Location import Location


class Projectile(Location):
    #x y
    #hitscan
    def __init__(self, x, y, dT):
        self.x = x
        self.y = y
        self.dT = dT

    def XYCollision(self):
        pass

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def projectileDistance(self, dT):
        c = Projectile(self.x + dT, self.y + dT)
        return c

    def isCollide(self, projDistance, otherProj):
        x = projDistance.x - self.x
        y = projDistance.y - self.y
        x1 = otherProj.x
        y1 = otherProj.y
        #xOrigin = 0 xFinal = 10 otherLoc = 5
        
