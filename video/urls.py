from django.urls import path
from . import views
from .views import (
    PlaylistCreateView,
)



urlpatterns = [
    path('video/', views.home, name='video-home'),
    path('video/createplaylist/', PlaylistCreateView.as_view(), name='playlist-create'),
]