from django import forms
from django.contrib.auth.models import User
from .models import Story, Note, Comment

"""
Form module contains class definitions for forms a user may fill out later
"""


class StoryForm(forms.ModelForm):
    """
    StoryFrom defines information a user has to provide to write a new story
    """

    class Meta:
        model = Story
        fields = {'artist', 'title', 'genre', 'text', }


class UserForm(forms.ModelForm):
    """
    UserForm defines information a user has to provide register a new user
    """

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class NoteForm(forms.ModelForm):
    """
    NoteForm defines information a user has to provide to write a new note
    """

    class Meta:
        model = Note
        fields = ['title', 'text', ]


class CommentForm(forms.ModelForm):
    """
    CommentForm defines information a user has to provide to write a new comment for a story
    """

    class Meta:
        model = Comment
        fields = ['comment']
