from django.urls import path, include
from . import views

app_name = 'todoapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),

]