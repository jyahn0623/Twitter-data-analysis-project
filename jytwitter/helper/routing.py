from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from . import consumers


websocket_urlpatterns = [
     url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]

application = ProtocolTypeRouter({
    # http -> django views is added by default
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})


