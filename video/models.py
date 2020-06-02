from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile

# Create your models here.
class Playlist(models.Model):
    creator=models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_playlist')
    name=models.CharField(max_length=100)
    viewed_by=models.ManyToManyField(UserProfile, related_name="viewed_playlists")
    size=models.IntegerField()
    Tags=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Comment(models.Model):
    posted_by=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text=models.CharField(max_length=100)
    replies=[]


class Video(models.Model): 

    video=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    upvotes=models.IntegerField()
    comments=models.ForeignKey(Comment, on_delete=models.CASCADE)
    views=models.IntegerField()