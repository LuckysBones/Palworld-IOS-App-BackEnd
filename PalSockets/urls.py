# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("player/", views.players , name="players"),
    path("metric/", views.metric, name="metric"),
]