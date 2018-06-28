from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

"""
Urls module defines the urlpatterns that can be used to access the application
"""

app_name = 'story'

urlpatterns = [

    path('story', views.index, name='index'),

    path('note', views.note, name='note'),

    path('register', views.register, name='register'),

    path('login', LoginView.as_view(), name='login_user'),

    path('logout', LogoutView.as_view(), name='logout_user'),

    path('story/<story_id>/detail', views.detail, name='detail'),

    path('note/<note_id>/detail', views.note_detail, name='note_detail'),

    path('story/add/', views.create_story, name='create_story'),

    path('note/add/', views.create_note, name='create_note'),

    path('story/<story_id>/delete', views.delete_story, name='delete_story'),

    path('note/<note_id>/delete', views.delete_note, name='delete_note'),

    path('note/<note_id>/update', views.update_note, name='update_note'),

    path('display', views.display, name='display_all'),

    path('comment/<story_id>/add', views.create_comment, name='create_comment'),

]
