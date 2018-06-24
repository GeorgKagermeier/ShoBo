from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'story'

urlpatterns = [

    path('story', views.index, name='index'),

    path('register', views.register, name='register'),

    path('login', LoginView.as_view(), name='login_user'),

    path('logout', LogoutView.as_view(), name='logout_user'),

    path('story/<int:story_id>/detail', views.detail, name='detail'),

    path('story/<int:note_id>/detail', views.note_detail, name='note_detail'),

    path('story/add/', views.create_story, name='create_story'),

    path('story/note/add/', views.create_note, name='create_note'),

    path('story/<story_id>/delete/', views.delete_story, name='delete_story'),

    path('story/<note_id>/delete/', views.delete_note, name='delete_note'),


]
