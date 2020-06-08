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
        'playlists': Playlist.objects.all()
    }
    return render(request, 'video/home.html', context)

class PlaylistCreateView(CreateView):
    model = Playlist
    fields = ['name', 'Tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)