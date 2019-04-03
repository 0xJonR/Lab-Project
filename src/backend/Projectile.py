from .Location import Location


class Orientation(): # use orientation("up")
    # access orientation of an object with object.orient
    def __init__(self, orient):  # up down left right upleft upright downleft downright
        self.orientString = orient
        if orient == "up":
            self.orient = (0, -1)
        elif orient == "down":
            self.orient = (0, 1)
        elif orient == "left":
            self.orient = (-1, 0)
        elif orient == "right":
            self.orient = (1, 0)
        elif orient == "upleft":
            self.orient = (-1, -1)
        elif orient == "upright":
            self.orient = (1, -1)
        elif orient == "downleft":
            self.orient = (-1, 1)
        elif orient == "downright":
            self.orient = (1, 1)

    def update(self, orient):
        super(orient)

    def to_dict(self):
        return {"orientation": self.orientString}

    def to_json(self):
        import json
        return json.dumps(self.to_dict())
# TODO: WRITE TEST CASE AND ENSURE ORIENTATION WORKS AS INTENDED
# INTENT FOR ORIENTATION CLASS: AUTOMATICALLY CONFIGURE PROJECTILES DIRECTION.
#  8 DIFFERENT WAYS A PROJECTILE CAN MOVE, WITH EFFECT IT'S LINE SEGMENT
#       ORIENTATION NOW ALSO SIMPLIFIES ORIENTATION LATER FOR CHARACTER: JUST EXTEND
#  PROPER LINE SEGMENT IS REQUIRED FOR COLLISION DETECTION


class Projectile(Orientation, Location):
    # param x y = location
    # param fD = weapon fireDistance# hitscan
    # param orientation = orientation
    def __init__(self, x, y, fd, orientation):
        self.x = x
        self.y = y
        self.fireDistance = fd
        super().__init__(orientation)
        # thinks its calling super to Location, we want Orientation

    # USE SELF.DISTANCE TO GET EXPECTED RANGE OF PROJECTILE AND GO POINT BY POINT
    # TO CHECK FOR COLLISION
    # returns resulting location
    def distance(self):
        xbias = self.orient[0]
        ybias = self.orient[1]
        c = Location(self.x + (self.fireDistance * xbias), self.y + (self.fireDistance * ybias))
        return c

    def collision(self, amap):
        from .myMap import myMap
        # check point by point until collision (occupiesSpace) end of fireDistance
        # use orientation to know if up or left or etc
        dist = self.distance() # Location (x, y) of projectile path
        i = self.x
        j = self.y
        while i <= dist.x and j <= dist.y:
            if i == dist.x and dist.y > j:
                if not amap.world[i][j+1].occupiesSpace:  # down
                    j += 1
                else:
                    return True
            elif j == dist.y and dist.x > i:
                if not amap.world[i+1][j].occupiesSpace:  # right
                    i += 1
                else:
                    return True
            elif i == dist.x and dist.y < j:
                if not amap.world[i][j-1].occupiesSpace:  # up
                    j -= 1
                else:
                    return True
            elif j == dist.y and dist.x < i:
                if not amap.world[i-1][j].occupiesSpace:  # left
                    i -= 1
                else:
                    return True
            elif dist.x > i and dist.y > j:  # downright
                if not amap.world[i+1][j+1].occupiesSpace:
                    i += 1
                    j += 1
                else:
                    return True
            elif dist.x < i and dist.y > j:  # downleft
                if not amap.world[i-1][j+1].occupiesSpace:
                    i -= 1
                    j += 1
                else:
                    return True
            elif dist.x > i and dist.y < j:  # upright
                if not amap.world[i+1][j-1].occupiesSpace:
                    i += 1
                    j -= 1
                else:
                    return True
            elif dist.x < i and dist.y < j:  # upleft
                if not amap.world[i-1][j-1].occupiesSpace:
                    i -= 1
                    j -= 1
                else:
                    return True
        return False

    def result(self, amap):  # returns new location after projectile
        if self.collision(amap):
            pass
        else:
            return self.distance(self)
