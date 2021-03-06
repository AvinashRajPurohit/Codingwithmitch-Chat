from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path

from chat.consumers import ChatConsumer
from notification.consumers import NotificationConsumer
from public_chat.consumers import PublicChatConsumer

application = ProtocolTypeRouter({
	'websocket': AllowedHostsOriginValidator(
		AuthMiddlewareStack(
			URLRouter([
					path('', NotificationConsumer),
					path('chat/<room_id>/', ChatConsumer),
					path('public_chat/<room_id>/', PublicChatConsumer),
				])
		)
	),
})









