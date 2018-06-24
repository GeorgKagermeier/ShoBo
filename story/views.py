from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StoryForm, UserForm, NoteForm
from .models import Story, Note


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        stories = Story.objects.filter(user=request.user)
        story_results = Story.objects.all()
        query = request.GET.get("q")
        if query:
                return render(request, 'story/index.html', {
                    'stories': story_results,
                })
        else:
            return render(request, 'story/index.html', {'stories': stories})


def create_story(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return render(request, 'story/detail.html',  {'story': story})
        context = {
            "form": form,
        }
        return render(request, 'story/create_story.html', context)


def create_note(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return render(request, 'story/note_detail.html',  {'note': note})
        context = {
            "form": form,
        }
        return render(request, 'story/create_note.html', context)


def delete_story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    story.delete()
    story = Story.objects.filter(user=request.user)
    return redirect('story:index')


def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    note = Note.objects.filter(user=request.user)
    return redirect('story:index')


def detail(request, story_id):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        user = request.user
        story = get_object_or_404(Story, pk=story_id)
        ctx = {'story': story, 'user': user}
    return render(request, 'story/detail.html', context=ctx)


def note_detail(request, note_id):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        user = request.user
        note = get_object_or_404(Note, pk=note_id)
        ctx = {'note': note, 'user': user}
    return render(request, 'story/note_detail.html', context=ctx)


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect(request, 'registration/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                stories = Story.objects.filter(user=request.user)
                notes = Note.objects.filter(user=request.user)
                return render(request, 'story/index.html', {'stories': stories}, {'notes': notes})
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
                notes = Note.objects.filter(user=request.user)
                return render(request, 'story/index.html', {'stories': stories}, {'notes': notes})
    context = {
        "form": form,
    }
    return render(request, 'story/register.html', context)





