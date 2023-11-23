import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.security.websocket import AllowedHostsOriginValidator
from django.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django_asgi_app = get_asgi_application()

import stats.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                stats.routing.websocket_urlpatterns
            )
        )
    )
})