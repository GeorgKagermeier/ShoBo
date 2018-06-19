from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import StoryForm, UserForm, NoteForm
from .models import Story


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        stories = Story.objects.order_by('-date_added')
        context = {'stories': stories}
        return render(request, 'story/index.html', context)


def create_story(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        form = StoryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
                story = form.save(commit=False)
                story.user = request.user
                story.save()
                return render(request, 'story/detail.html', {'story': story})
        context = {
            "form": form,
        }
        return render(request, 'story/create_story.html', context)


def delete_story(request, story_id):
    story = Story.objects.get(pk=story_id)
    story.delete()
    story = Story.objects.filter(user=request.user)
    return render(request, 'story/index.html', {'story': story})


def detail(request, story_id):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        user = request.user
        story = get_object_or_404(Story, pk=story_id),
    return render(request, 'story/detail.html', {'story': story, 'user': user})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'registration/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                stories = Story.objects.filter(user=request.user)
                return render(request, 'story/index.html', {'stories': stories})
            else:
                return render(request, 'registration/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    return render(request, 'registration/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                stories = Story.objects.filter(user=request.user)
                return render(request, 'story/index.html', {'stories': stories})
    context = {
        "form": form,
    }
    return render(request, 'story/register.html', context)
