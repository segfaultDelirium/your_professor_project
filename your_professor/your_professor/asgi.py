"""
ASGI config for your_professor project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from asgi_cors_middleware import CorsASGIApp


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_professor.settings')

application = get_asgi_application()
application = CorsASGIApp(
    app = application,
    origins=["localhost:4200"]
)