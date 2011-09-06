import math
import random

class Actor(object):
    x, y = 0, 0

    def get_id(self):
        raise Exception('get_id() method should be implemented')

    def move(self , map):
        pass

class RandomMovingActor(Actor):

    """This class is used to represent logic of computer-controlled actors."""

    direction, speed = 0, 0

    def __init__(self, id, x, y, *args, **kwargs):
        super(RandomMovingActor, self).__init__(*args, **kwargs)
        self.id = id
        self.x  = x
        self.y  = y
        self.randomize_movement()

    def randomize_movement(self):
        self.direction = random.randint(0, 359)
        self.speed     = random.randint(1, 5)/10.

    def get_id(self):
        return self.id

    def move(self, map):
        rad = self.direction / 180. * math.pi
        new_x = self.x + math.cos(rad) * self.speed
        new_y = self.y + math.sin(rad) * self.speed
        if map.can_move(new_x, new_y):
            self.x, self.y = new_x, new_y
            #print "UserID=%s pos(%d,%d)" % (self.get_id(), self.x, self.y)
        else:
            self.randomize_movement()

class UserActor(Actor):

    """This class is used to represent logic of human-controlled actors."""
    
    def __init__(self, sock, id):
        self.sock = sock
        self.id   = id
        self.new_x, self.new_y = self.x, self.y

    def get_id(self):
        return self.id

    def move(self, map):
        dx, dy = self.new_x - self.x, self.new_y - self.y
        gip    = math.sqrt(math.pow(dx,2) + math.pow(dy, 2))
        moved  = False
        if gip > 0.001:
            rad_x = math.acos(dx/gip)
            rad_y = math.asin(dy/gip)
            new_x = self.x + math.cos(rad_x) * 0.1
            new_y = self.y + math.sin(rad_y) * 0.1
            if map.can_move(new_x, new_y):
                self.x, self.y = new_x, new_y
                moved = True
        if not moved:
            self.new_x, self.new_y = self.x, self.y

    def moveto(self, x, y):
        #self.x, self.y = x, y
        self.new_x, self.new_y = x, y
