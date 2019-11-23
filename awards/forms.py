from django import forms
from .models import Profile, Projects, Rates

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'image_landing', 'description', 'link')