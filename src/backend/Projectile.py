from .Location import Location


class Orientation(): #use orientation("up")
    #access orientation of an object with object.orient
    def __init__(self, orient): #up down left right upleft upright downleft downright
        self.orientString = orient
        if (orient == "up"):
            self.orient = (0, 1)
        elif orient == "down":
            self.orient = (0, -1)
        elif orient == "left":
            self.orient = (-1, 0)
        elif orient == "right":
            self.orient = (1, 0)
        elif orient == "upleft":
            self.orient = (-1, 1)
        elif orient == "upright":
            self.orient = (1, 1)
        elif orient == "downleft":
            self.orient = (-1, -1)
        elif orient == "downright":
            self.orient == (1, -1)

#TODO: WRITE TEST CASE AND ENSURE ORIENTATION WORKS AS INTENDED
#INTENT FOR ORIENTATION CLASS: AUTOMATICALLY CONFIGURE PROJECTILES DIRECTION.
# 8 DIFFERENT WAYS A PROJECTILE CAN MOVE, WITH EFFECT IT'S LINE SEGMENT
#      ORIENTATION NOW ALSO SIMPLIFIES ORIENTATION LATER FOR CHARACTER: JUST EXTEND
# PROPER LINE SEGMENT IS REQUIRED FOR COLLISION DETECTION
#END TODO

class Projectile(Location, Orientation):
    #x y = location
    #param fD = weapon fireDistance
    #hitscan
    #
    def __init__(self, x, y, fd, orientation):
        self.x = x
        self.y = y
        self.fireDistance = fd
        super().__init__(orientation)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def distance(self):
        xbias = self.orient[0]
        ybias = self.orient[1]
        c = Projectile((self.x + self.fireDistance) * xbias, (self.y + self.fireDistance) * ybias)
        return c

    #TODO FINISH THIS FUNCTION
    def collision(self, projDistance, otherProj):
        #check point by point until collision (occupiesSpace) end of fireDistance
        #use orientation to know if up or left or etc
        pass

