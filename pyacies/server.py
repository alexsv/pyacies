from components import GameMap, Actors
from circuits import Debugger
from circuits.web import Server, Controller
from interactions import WebSocketServer

class Root(Controller):
    def __init__(self, *args, **kwargs):
        super(Root, self).__init__(*args, **kwargs)
        f = open('../www/game.html', 'rb')
        self.html = "\n".join(f.readlines())
        f.close()

    def index(self):
        #f = open('../www/game.html', 'rb')
        #self.html = "\n".join(f.readlines())
        #f.close()
        return self.html

(GameMap()
 +WebSocketServer(('0.0.0.0', 8000))
 +Root()
 +Actors()
 #+Debugger()
).run()