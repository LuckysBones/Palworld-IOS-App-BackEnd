from django.urls import path
from . import consumers 

ws_patterns = [
    path('ws/players/', consumers.PlayersConsumer.as_asgi()),
    path('ws/info/', consumers.InfoConsumer.as_asgi()),
    path('ws/metric/', consumers.MetricConsumer.as_asgi()),
    path('ws/message/', consumers.MessageConsumer.as_asgi()),
    path('ws/save/', consumers.SaveConsumer.as_asgi()),
    path('ws/shutdown/', consumers.ShutdownConsumer.as_asgi()),
    
]
