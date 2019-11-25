from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Projects, Rates, Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileEditForm, ProjectUploadForm, VotesForm, ReviewForm
from django.shortcuts import get_object_or_404
# from .permissions import IsAdminOrReadOnly

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'index.html', context)

def projects(request, pk):
    current_user = request.user
    project = Projects.objects.get(pk=pk)
    rate = Rates.get_rates(project.id)
    form = VotesForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            rate = form.save(commit=False)
            rate.user = current_user
            rate.project = project
            rate.project_id = project.id
            rate.save()
            return redirect('index')
    else:
        form = VotesForm()
    
    return render(request, 'single_post.html', {'form':form, 'project':project, 'rate':rate})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    profile = User.objects.get(username = username)

    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    return render(request, 'profile/profile.html', {"profile":profile, "profile_details":profile_details, "projects":projects})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    title = 'Edit Profile'
    profile = User.objects.get(username=request.user)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile', username=request.user)
    else:
        form = ProfileEditForm()

    return render(request, 'profile/edit_profile.html', {"form":form, "profile_details":profile_details})

@login_required(login_url='/accounts/login/')
def post_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile = current_user
            form.save()
        return redirect('home')
    else:
        form = ProjectUploadForm()

    return render(request, 'uploads.html', {"form":form,})

def search_results(request):
    if 'titles' in request.GET and request.GET['titles']:
        search_term = request.GET.get("titles")
        searched_projects = Projects.search_by_projects(search_term)

        message = f'{search_term}'

        return render(request, 'search.html', {"message":message, "projects":searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message, "projects":searched_projects})