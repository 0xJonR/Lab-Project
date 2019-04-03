class Location:
    #    attributes
    occupiesSpace = False #true by default
    overWritable = True #to be used in spawn generation
    #    init
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_json(self):
        import json
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {'x':self.x, 'y':self.y}
#    #instance methods


class Rock(Location):

    occupiesSpace = True

    def __init__(self, loc):
        self.x = loc.x
        self.y = loc.y


class Crate(Location):

    occupiesSpace = True

    def __init__(self, loc):
        self.x = loc.x
        self.y = loc.y

