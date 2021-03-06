"""
Views module containing methods to display views for templates and models
"""
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from .forms import StoryForm, UserForm, NoteForm, CommentForm
from .models import Story, Note, Comment


def index(request):
    """
        Display a landing page for user which are logged in only the stories`.

        **Template:**

        :template:`story/templates/story/index.html`
    """
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        stories = Story.objects.filter(user=request.user)
        story_results = Story.objects.all()
        query = request.GET.get("q")
        if query:
            return render(request, 'story/index.html', {
                'stories': story_results
            })
        else:
            return render(request, 'story/index.html', {'stories': stories})


def note(request):
    """
           Display a landing page for user which are logged in only the notes`.

           **Template:**

           :template:`story/templates/story/note.html`
       """
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        notes = Note.objects.filter(user=request.user)
        return render(request, 'story/note.html', {
            'notes': notes
        })


def create_story(request):
    """
       Display a form to create a new story for a user that is logged in

       **Template:**

       :template:`story/templates/story/create_story.html`
    """
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.user = request.user
            story.save()
            return redirect('story:index')
        context = {
            "form": form,
        }
        return render(request, 'story/create_story.html', context)


def create_note(request):
    """
          Display a form to create a new note for a user that is logged in

          **Template:**

          :template:`story/templates/story/create_note.html`
    """
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return render(request, 'story/note_detail.html', {'note': note})
        context = {
            "form": form,
        }
        return render(request, 'story/create_note.html', context)


def create_comment(request, story_id):
    """
          Display a form to create a new comment for a story for a user that is logged in

          **Template:**

          :template:`story/templates/story/create_comment.html`
    """

    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            story = get_object_or_404(Story, pk=story_id)

            comment = form.save(commit=False)
            comment.user = user
            comment.story = story
            comment.save()
            ctx = {'story': story, 'user': user, 'comment': comment}
            return render(request, 'story/detail.html', ctx)
        context = {
            "form": form,
        }
        return render(request, 'story/create_comment.html', context)


def delete_story(request, story_id):
    """
               Delete a story

               **Context**
               story_id of the story that should be deleted

    """
    story = get_object_or_404(Story, pk=story_id)
    story.delete()
    story = Story.objects.filter(user=request.user)
    return redirect('story:index')


def delete_note(request, note_id):
    """
                   Delete a note

                   **Context**
                   note_id of the note that should be deleted

    """
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    note = Note.objects.filter(user=request.user)
    return redirect('story:note')


def update_note(request, note_id):
    """
           Displays a form to update a note for a logged in user.

           **Context**
           note_id of the note that should be updated

           **Template:**

           :template:`story/templates/story/update_note.html`
    """
    note = get_object_or_404(Note, pk=note_id)
    form = NoteForm(request.POST or None, instance=note)

    if form.is_valid():
        form.save()
        return redirect('story:note')

    ctx = {'form': form, 'note': note}
    return render(request, 'story/create_note.html', context=ctx)


def detail(request, story_id):
    """
              Displays the detail page of a story for a logged in user.

              **Context**
              story_id of the story that should be displayed

              **Template:**

              :template:`story/templates/story/detail.html`
    """
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        user = request.user
        story = get_object_or_404(Story, pk=story_id)
        comment = Comment.objects.select_related('story').order_by('-date_commented')
        filtered = comment.filter(story_id=story_id)
        ctx = {'story': story, 'user': user, 'comments': filtered}
        print(ctx)
    return render(request, 'story/detail.html', context=ctx)


def note_detail(request, note_id):
    """
                Displays the detail page of a note for a logged in user.

                **Context**
                note_id of the note that should be displayed

                **Template:**

                :template:`story/templates/story/note_detail.html`
      """

    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        user = request.user
        note = get_object_or_404(Note, pk=note_id)
        ctx = {'note': note, 'user': user}
    return render(request, 'story/note_detail.html', context=ctx)


def logout_user(request):
    """
                    Logout function

          """
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect(request, 'registration/login.html', context)


def login_user(request):
    """
                Displays the login page of a user to get logged in.


                **Template:**

                :template:`story/templates/registration/login.html`
      """
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
    """
                   Displays the register page of a new user to get registered.


                   **Template:**

                   :template:`story/templates/story/register.html`
         """
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


def display(request):
    """
                    Display all stories by all users written. Only registered users can view the stories


                    **Template:**

                    :template:`story/templates/story/display.html`
          """
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        stories = Story.objects.filter(user=request.user)
        story_results = Story.objects.all()
        query = request.GET.get("q")
        if query:
            return render(request, 'story/display.html', {
                'stories': story_results
            })
        else:
            return render(request, 'story/display.html', {'stories': stories})
