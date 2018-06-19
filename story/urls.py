from django.urls import path
from . import views

app_name = 'story'

urlpatterns = [

    path('story', views.index, name='index'),

    path('register', views.register, name='register'),

    path('login_user', views.login_user, name='login_user'),

    path('logout_user', views.logout_user, name='logout_user'),

    path('story/<int:story_id>', views.detail, name='detail'),
    # /story/story/add/
    path('story/add/', views.create_story, name='create_story'),
    # /story/story/2/
    #path('story/<int:story_id>/$', views.update_story, name='update_story'),
    # /story/story/2/delete/
    path('story/<int:story_id>/delete/', views.delete_story, name='delete_story'),

]
