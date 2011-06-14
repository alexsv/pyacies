
class Map(object):
    actors = []
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def can_move(self, x, y):
        return x > 0 and y > 0 and x < self.width and y < self.width