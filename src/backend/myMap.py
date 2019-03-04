from .Projectile import Projectile
from .Character import Character
from .Location import Location

#matrix[column][row]
#origin is [0][0] top left corner: right to left movement is map[+-x][row]
#up to down movement is map[x][+-y]
class myMap():

    def __init__(self, size):
        world = [[0 for j in range(size)] for i in range(size)]
        for row_index, row in enumerate(world):
            for col_index, item in enumerate(row):
                world[row_index][col_index] = Location(row_index, col_index)
                #inits world full of locations


    def addChar(self, dropzoneX, dropZoneY):
        world[dropzoneX][dropZoneY] = Character(dropzoneX, dropZoneY)
        pass
