from django.urls import path
from . import views
from .views import (
    PlaylistCreateView,
    
)
from video.views import(

	upload_video_view,
	detail_video_view,
	update_video_view,

)

app_name = 'video'

urlpatterns = [
    path('video/', views.home, name='video-home'),
    path('video/createplaylist/', PlaylistCreateView.as_view(), name='playlist-create'),
    path ('upload/',upload_video_view,name="upload"),
	path ('<slug>/',detail_video_view,name="detail"),
	path ('<slug>/update',update_video_view,name="update"),
]







