from django import forms
from .models import Profile, Projects, Rates, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'image_landing', 'description', 'link')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class VotesForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ('design', 'usability', 'content')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comments',)