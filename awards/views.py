from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Profile, Projects, Rates
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileEditForm, ProjectUploadForm, VotesForm, ReviewForm
from .permissions import IsAdminOrReadOnly

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'index.html', context)

def projects(request, project_id):
    try:
        projects = Projects.objects.get(id = project_id)
        all = Rates.objects.filter(project=project_id)
    except Exception as e:
        raise Http404()

    #single user votes count
    count = 0
    for i in all:
        count+=i.usability
        count+=i.design
        count+=i.content

    if count > 0:
        average = round(count/3,1)
    else:
        average = 0

    if request.method == 'POST':
        form = VotesForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project_id
            rate.save()
        return redirect('projects', project_id)

    else:
        form = VotesForm()

    # The votes logic
    votes = Rates.objects.filter(project=project_id)
    usability = []
    design = []
    content = []

    for i in votes:
        usability.append(i.usability)
        design.append(i.design)
        content.append(i.content)

    if len(usability) > 0 or len(design) > 0 or len(content) > 0:
        average_usability = round(sum(usability)/len(usability),1)
        average_design = round(sum(design)/len(design), 1)
        average_content = round(sum(content)/len(content), 1)

        average_rating = round((average_content+average_design+average_usability)/3, 1)


    else:
        average_content = 0.0
        average_design = 0.0
        average_usability = 0.0
        average_rating = 0.0


    # To make sure that a user only votes once
    arr1 = []
    for use in votes:
        arr1.append(use.user_id)

    auth = arr1

    reviews = ReviewForm(request.POST)
    if request.method == 'POST':
        if reviews.is_valid():
            comment = reviews.save(commit = False)
            comment.user = request.user
            comment.save()
            return redirect('projects', project_id)
        else:
            reviews = ReviewForm()

    user_comments = Comments.objects.filter(pro_id=project_id)

    context = {
        'projects':projects,
        'form':form,
        'usability':average_usability,
        'design':average_design,
        'content':average_content,
        'average_rating':average_rating,
        'auth':auth,
        'all':all,
        'average':average,
        'comments':user_comments,
        'reviews':reviews,
    }
    return render(request, 'single_post.html', context)