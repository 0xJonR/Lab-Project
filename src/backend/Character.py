from .Location import Location
#TODO ADD ALL FUNCTIONALITY
from .Projectile import Orientation, Projectile
import keyboard


class Character(Location):

    def __init__(self, loc):
        self.location = loc  # determines location of character
        self.health = 1000  # determines health of character
        self.armor = 0  # determines armor of character
        self.speed = 1  # determines speed of character
        self.inventory = [] # determines inventory of character
        self.guns = []  # determines guns of character
        self.orient = Orientation("up")  # determines orient of character

    def pickup(self, item): #API: add item to inventory
        self.inventory.append(item)

    def get_movement(self, amap):  # listen for key press, return new location based on key
        # WASD movement
        if keyboard.is_pressed('w'):
            self.orient_handler('up')
            self.location = self.movement_handler('up').result(amap)
        elif keyboard.is_pressed('s'):
            self.orient_handler('down')
            self.location = self.movement_handler('down').result(amap)
        elif keyboard.is_pressed('a'):
            self.orient_handler('left')
            self.location = self.movement_handler('left').result(amap)
        elif keyboard.is_pressed('d'):
            self.orient_handler('right')
            self.location = self.movement_handler('right').result(amap)
 
    def orient_handler(self, string): #orientation
        if string == 'w':
            self.orient.update("up")

        elif string =='s':
            self.orient.update('down')

        elif string =='a':
            self.orient.update("left")

        elif string =='d':
            self.orient.update("right")

    def movement_handler(self, direction):
        if direction == self.orient.orientString:
            return Projectile(self.location.x, self.location.y, self.speed, self.orient)
        else:
            pass

    def to_json(self):  # imports character info into Json
        pass

