from django.db import models
from django.contrib.auth.models import User
from user.models import UserProfile
from django_slugify_processor.text import slugify
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_delete, pre_save



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


def upload_location(instance,filename,**kwargs):
	file_path ='video/{author_id}/{title}-{filename}'.format(
			author_id=str(instance.author.id),title=str(instance.title),filename=filename
		)
	return file_path


class VideoUpload(models.Model):
	title						= models.CharField(max_length=50, null=False, blank=False)
	body						= models.TextField(max_length=5000, null=False, blank=False)
	videofile					= models.FileField(upload_to=upload_location, null=True, verbose_name="")
	date_published				= models.DateTimeField(auto_now_add=True,verbose_name="date published")
	date_updated				= models.DateTimeField(auto_now_add=True,verbose_name="date  updated")
	author						= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	slug						= models.SlugField(blank=True ,unique=True)


	def __str__(self):
		 return self.title 

@receiver(post_delete,sender=VideoUpload)
def submission_delete(sender,instance,**kwargs):
	instance.videofile.delete(False)


def pre_save_upload_video_receiever(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.author.username + "-"+instance.title)


pre_save.connect(pre_save_upload_video_receiever,sender=VideoUpload)

