from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'story'

urlpatterns = [

    path('story', views.index, name='index'),

    path('register', views.register, name='register'),

    path('login', LoginView.as_view(), name='login_user'),

    path('logout', views.logout, name='logout_user'),

    path('story/<int:story_id>', views.detail, name='detail'),
    # /story/story/add/
    path('story/add/', views.create_story, name='create_story'),
    # /story/story/2/
    #path('story/<int:story_id>/$', views.update_story, name='update_story'),
    # /story/story/2/delete/
    path('story/<int:story_id>/delete/', views.delete_story, name='delete_story'),

]
