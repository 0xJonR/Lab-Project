class Location:
    #    attributes
    occupiesSpace = True #true by default
    #    init
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

#    #instance methods
