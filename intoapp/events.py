from socketio.namespace import BaseNamespace
from django_socketio.events import Namespace
from socketio.mixins import BroadcastMixin


@Namespace('/echo')
class EchoNamespace(BaseNamespace, BroadcastMixin):
    nicknames = []

    def initialize(self):
        pass

    def on_echo(self, echo):
        self.broadcast_event('echo', echo)

    def recv_disconnect(self):
        self.log('Disconnected')
        self.disconnect(silent=True)
        return True