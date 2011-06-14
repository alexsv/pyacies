from components import GameMap, Actors
from circuits import Debugger
from circuits.web import Server
from interactions import WebSocketServer

(GameMap()
 +WebSocketServer(('127.0.0.1', 8000))
 +Actors()
 +Debugger()
).run()