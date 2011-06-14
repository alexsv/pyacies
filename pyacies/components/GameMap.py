from circuits import Component, Timer, Event
from core.maps import Map
from core.actors import RandomMovingActor

TIME_STEP = 1

class GameMap(Component):

    channel = 'gamemap'

    map    = None
    actors = {}

    def __init__(self, *args, **kwargs):
        super(GameMap, self).__init__(*args, **kwargs)
        Timer(TIME_STEP, Event(), persist=True).register(self)
        
        # map initialization
        self.map = Map(100, 50)
        self.map.actors = self.actors
        for i in xrange(2):
            actor = RandomMovingActor('actor'+str(i), 0, 0)
            self.actors[actor.get_id()] = actor

    def started(self, *args):
        print 'STARTED', args

    def stopped(self, *args):
        print 'STOPPED'

    def event(self, *args, **kwargs):
        print 'GOT', self.channel

    def timer(self):
        """ Fires on each timer tick. Performs moving of computer actors(bots)."""
        if self.map:
            for actor_id, actor in self.actors.iteritems():
                self.fire(Event(actor=actor, map=self.map), 'timer', target='actors')
            self.fire(Event(map=self.map), 'redraw', target='*')

    def connect_user(self, user=None):
        self.actors[user.get_id()] = user

    def disconnect_user(self, user=None):
        del self.actors[user.get_id()]

    def redraw_actor(self, actor=None):
        if hasattr(actor, 'sock'):
            print 'REDRAW_ACTOR', actor.get_id()
            #should be only for actors with socket
            self.fire(Event(actor=actor, map=self.map), 'redraw_actor', target='interactions')

