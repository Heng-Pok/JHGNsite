from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('greet', views.greet, name='greet'),
    path('notes/', views.note_list, name='note_list'),
    path('notes/create/', views.create_note, name='create_note'),
]