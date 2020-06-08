from django.contrib import admin
from .models import Comment, Playlist, Video, VideoUpload

# Register your models here.

admin.site.register(Comment)
admin.site.register(Playlist)
admin.site.register(Video)
admin.site.register(VideoUpload)
