"""
ASGI config for PalLensBackEnd project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from PalSockets.routing import ws_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PalLensBackEnd.settings')

pallen_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        'http': pallen_asgi_app,
        'websocket': AuthMiddlewareStack(
            URLRouter(
                ws_patterns
            )
        )
    }
)
