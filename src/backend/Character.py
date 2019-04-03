from .Location import Location
#TODO ADD ALL FUNCTIONALITY
from .Projectile import Orientation
import keyboard

class Character(Location):
    health = 1000
    speed = 10
    inventory = []
    orient = Orientation("up") #default orient
    def pickup(self, item):
        pass
    def getMovement(self): #listen for key press, return new location based on key
        #W A S D movement
        if keyboard.is_pressed('w'):
            self.movement_handler('up')
        elif keyboard.is_pressed('s'):
            self.movement_handler('down')
        elif keyboard.is_pressed('a'):
            self.movement_handler('left')
        elif keyboard.is_pressed('d'):
            self.movement_handler('right')
 
    def movement_handler(self, string):
        if string == 'w':

            #doThis
        elif string =='s':
            #dothis
        elif string =='a':
            #dothis
        elif string =='d':
            #dothis


    def toJson(): #imports character info into Json
        pass
