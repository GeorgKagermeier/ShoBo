from django import forms
from django.contrib.auth.models import User

from .models import Story


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
        name = forms.CharField(max_length=20)
        note = forms.CharField(widget=forms.Textarea())
