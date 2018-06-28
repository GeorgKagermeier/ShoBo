from django import forms
from django.contrib.auth.models import User
from .models import Story, Note, Comment


class StoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = {'artist', 'title', 'genre', 'text', }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'text', ]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
