from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Projects, Rates
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileEditForm, ProjectUploadForm, VotesForm

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'index.html', context)
