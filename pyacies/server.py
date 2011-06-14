from components import GameMap, Actors
from circuits import Debugger

(GameMap()
 +Actors()
 +Debugger()
).run()