from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from user.models import UserProfile
from django.http import HttpResponse
from .models import Playlist, Video
from django.views.generic import (
    CreateView,
)





# Create your views here.
def home(request):
    context = {
        'playlist': Playlist.objects.all()
    }
    return render(request, 'video/home.html', context)

class PlaylistCreateView(CreateView):
    model = Playlist
    fields = ['name', 'Tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def upload_video_view(request):



	context = {}



	user = request.user
	if not user.is_authenticated:
		return redirect('must_authenticate')

	form =  UploadVideoForm(request.POST or None, request.FILES or None )
	if form.is_valid():
		obj = form.save(commit=False)
		author = Account.objects.filter(email=user.email).first()
		obj.author = author
		obj.save()
		form = UploadVideoForm()


	context['form'] = form


	return render (request,"video/create_video.html",context)


def detail_video_view(request,slug):

	context = {}

	video_post = get_object_or_404(VideoUpload, slug=slug)
	context['video_post'] = video_post

	return render (request, 'video/detail_video.html', context)


def update_video_view(request,slug):

	context = {}

	user = request.user
	if not user.is_authenticated:
		return redirect("must_authenticate")

	video_post = get_object_or_404(VideoUpload,slug=slug)
	if video_post.author != user:
		return HttpResponse("You are not the auther of that post.")

	if request.POST:
		form = UpdateVideoForm(request.POST or None, request.FILES or None, instance=video_post)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			context['success_message'] = "Updated"
			video_post = obj
	form = UpdateVideoForm(
			initial = {
					"title": video_post.title,
					"body": video_post.body,
					"videofile": video_post.videofile,
			}
		)

	context['form'] = form
	return render (request,'video/update_video.html',context)


