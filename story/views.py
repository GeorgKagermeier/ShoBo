from django.http import Http404
from django.shortcuts import render
from .models import Story

def index(request):
    all_storys = Story.objects.all()
    return render(request, 'story/index.html', {'all_storys': all_storys})

def detail(request, story_id):
    try:
        story = Story.objects.get(pk=story_id)
    except Story.DoesNotExist:
        raise Http404("Story does not exist")
    return render(request, 'story/detail.html', {'story': story})
