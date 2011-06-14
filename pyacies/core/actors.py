

class Actor(object):
    def get_id(self):
        raise Exception('get_id() method should be implemented')

    def move(self , map):
        pass

class RandomMovingActor(Actor):

    """This class is used to represent logic of computer-controlled actors."""

    def __init__(self, id, x, y, *args, **kwargs):
        super(RandomMovingActor, self).__init__(*args, **kwargs)
        self.id = id
        self.x  = x
        self.y  = y

    def get_id(self):
        return self.id

    def move(self, map):
        pass

class UserActor(Actor):

    """This class is used to represent logic of human-controlled actors."""
    
    def __init__(self, sock, id):
        self.sock = sock
        self.id   = id

    def get_id(self):
        return self.id
