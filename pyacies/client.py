from circuits import Component, Debugger, Event
from core.actors import UserActor

class GameClient(Component):
    pass

(GameClient()
 +Debugger()
).run()