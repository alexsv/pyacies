from circuits import Event, handler
from circuits.web import Server
from circuits.web.dispatchers import WebSockets
from circuits.net.sockets import Write
from core.actors import UserActor

WEBSOCKET_PATH = '/ws'

class WebSocketServer(Server):

    connection_id = 0

    sock_users = {}
    
    def __init__(self, *args, **kwargs):
        super(WebSocketServer, self).__init__(*args, **kwargs)
        WebSockets(WEBSOCKET_PATH).register(self)
        print '* * * * ', self.channel

    def get_next_user_id(self):
        self.connection_id += 1
        return 'user' + str(self.connection_id)

    @handler('message', target='ws')
    def message(self, sock, data):
        if sock not in self.sock_users:
            user = UserActor(sock, self.get_next_user_id())
            self.sock_users[sock] = user
            self.fire(Event(user=user), 'connect_user', target='gamemap')

    @handler("disconnect", target="web")
    def disconnect(self, sock):
        if sock in self.sock_users:
            user = self.sock_users[sock]
            del self.sock_users[sock]
            self.fire(Event(user=user), 'disconnect_user', target='gamemap')

    @handler('redraw_actor', target='interactions')
    def redraw_actor(self, actor=None, map=None):
        print 'REDRAWING ACTOR', actor.get_id()
        self.fire(Write(actor.sock, 'redraw data'), target='ws')