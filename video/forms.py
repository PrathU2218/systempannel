from django import forms 


from video.models import VideoUpload


class UploadVideoForm(forms.ModelForm):

	class Meta:
		model  = VideoUpload
		fields = ['title','body','videofile']



class UpdateVideoForm(forms.ModelForm):


	class Meta:
		model = VideoUpload
		fields = ['title','body','videofile']

	def save(self, commit=True):
		video_post = self.instance
		video_post.title = self.cleaned_data['title']
		video_post.body = self.cleaned_data['body']

		if self.cleaned_data['videofile']:
			video_post.videofile = self.cleaned_data['videofile']

		if commit:
			video_post.save()
		return video_post