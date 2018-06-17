from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

import story
from .forms import  StoryForm, UserForm
from .models import Story


def create_story(request):
   # if not request.user.is_authenticated():
   #     return render(request, 'story/login.html')
   # else:
        form = StoryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return render(request, 'story/detail.html', {'story': story}),

        context = {
                "form": form,
        }
        return render(request, 'story/create_story.html', context)


def delete_story(request, story_id):
    story= Story.objects.get(pk=story_id)
    story.delete()
    story = Story.objects.filter(user=request.user)
    return render(request, 'story/index.html', {'story': story})

def detail(request, story_id):
    # if not request.user.is_authenticated():
    #    return render(request, 'story/login.html')
    # else:
        user = request.user
        story = get_object_or_404(Story, pk=story_id)
        return render(request, 'story/detail.html', {'story': story, 'user': user})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'story/login.html', context)

def index(request):
    #if not request.user.is_authenticated():
    #    return render(request, 'story/login.html')
    #else:
        storys = Story.objects.filter(user=request.user)
        query = request.GET.get("q")
        if query:
            storys = storys.filter(
                Q(story_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            return render(request, 'story/index.html', {
                'storys': storys,
            })
        else:
            return render(request, 'story/index.html', {'story': story})

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
                storys = Story.objects.filter(user=request.user)
                return render(request, 'story/index.html', {'storys': storys})
    context = {
        "form": form,
    }
    return render(request, 'story/register.html', context)