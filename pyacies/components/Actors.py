from circuits import Component, Event

class Actors(Component):

    channel = 'actors'

    def timer(self, map=None, actor=None):
        if map and actor:
            actor.move(map)
            self.fire(Event(actor=actor), 'redraw_actor', target='gamemap')

